import pandas as pd
import numpy as np
import scipy.optimize as so
from IPython.display import display

from src.projet_a.data import O_besoins, Al, A

np.set_printoptions(precision=1, suppress=True)





## 1)  Le problème de base___________________________________________________________________________________________________________________

"""
Création des Besoins
"""
valeur_nutri = A[:-1]
prix = A[-1] 


"""
Résolution du problème
"""
Result = so.linprog(prix, A_ub = -valeur_nutri, b_ub = -O_besoins, method = 'highs')





## 2)  Les 10%___________________________________________________________________________________________________________________
A_ub = -valeur_nutri
b_ub = -O_besoins
A_ub2 = valeur_nutri
b_ub2 = 1.1 * O_besoins

A_total = np.vstack((A_ub, A_ub2))
b_total = np.hstack((b_ub, b_ub2))

Result = so.linprog(prix, A_ub = -valeur_nutri, b_ub = -O_besoins, method = 'highs')


# Limite supérieure : 110 % des besoins
A_ub_inf = -valeur_nutri            # ≥ besoins <=> -valeurs ≤ -besoins
b_ub_inf = -O_besoins

# Limite supérieure : ≤ 110% des besoins
A_ub_sup = valeur_nutri
b_ub_sup = 1.1 * O_besoins

# Contrainte combinée
A_total = np.vstack((A_ub_inf, A_ub_sup))
b_total = np.hstack((b_ub_inf, b_ub_sup))

# Résolution avec nouvelles contraintes
Result = so.linprog(prix, A_ub=A_total, b_ub=b_total, method='highs')


# Vérification des apports réels
apports_obtenus = valeur_nutri @ Result.x  # produit matriciel
pourcentages = apports_obtenus / O_besoins * 100



"""
Tableau des résultats
"""
nutriments = ['Protéines', 'Lipides', 'Glucides', 'Calories', 'Fer', 'Calcium', 'Fibres']

df_resultats = pd.DataFrame({
    'Nutriment': nutriments,
    'Besoins': O_besoins,
    'Apport obtenu': apports_obtenus,
    '% des besoins': pourcentages})




## Affichage des résultats____________________________________________________________________________________________________________________

"""
Affichage du coup
"""
print("")
print( "Cout : ", Result.fun)
print("")


"""
Affichage des aliments
"""
u = np.where(Result.x > 0)[0]  # Qté opti sup à 0

for k in u:
    print(Al.index[k])  # Nom de l'aliment
    print('{:0.2f} g'.format(Result.x[k] * 100))  # Quantité optimale en grammes

def rename_aliment(name):
    return name.replace("–", "-").strip()


"""
Affichage du résumé nutritionnel
"""
print("\nRésumé nutritionnel :")
print(df_resultats.to_string(index=False))
