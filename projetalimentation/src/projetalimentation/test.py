import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so
from IPython.display import display
from __init__ import *

np.set_printoptions(precision=1, suppress=True)





#Lecture de la base de données
Al = pd.read_csv(
                'C:/Cours/Supply Chain/SC/projetalimentation/data/Aliments.csv', 
                sep=';', 
                index_col=0)

Al.iloc[[10*k for k in range(5)],:]
A = np.array(Al).T


#Entrée des besoins
valeur_nutri = A[:-1]
prix = A[-1]  # Prix
besoins = np.array([75, # Proteines
                90, # Lipides
                225, # Glucides
                2000, # Calories
                9, # Fer
                800, # Calcium 
                45]) # Fibre


# Résolution du problème d'optimisation
Result = so.linprog(prix, A_ub = -valeur_nutri, b_ub = -besoins, method = 'highs')


# Affichage basique des résultats
print( "Cout minimal : ", Result.fun)
print("Quantité optimale : ", Result.x)


# Affichage avancé des résultats
u = np.where(Result.x > 0)[0]  # Qté opti sup à 0

for k in u:
    print(Al.index[k])  # Nom de l'aliment
    print('{:0.2f} g'.format(Result.x[k] * 100))  # Quantité optimale en grammes

def rename_aliment(name):
    return name.replace("–", "-").strip()

Phrase = 'Un repas est constitué de '
for s in range(len(u) - 1):
    if s > 0:
        Phrase += ','
    gr = Result.x[u[s]] * 100  # Quantité optimale en grammes
    old_name = Al.index[u[s]]  # Nom de l'aliment
    name = rename_aliment(old_name)  # Renommer l'aliment (fonction existante)
    Phrase += ' de {:0.2f} g de {}'.format(gr, name)


## Dernier aliment
s = len(u) - 1
gr = Result.x[u[s]] * 100
old_name = Al.index[u[s]]
name = rename_aliment(old_name)
Phrase += ' et de {:0.2f} g de {}. '.format(gr, name)
Phrase += ' Il coûte un total de {:0.2f} euros.'.format(Result.fun)

print(Phrase)





## 2)  Les 10%___________________________________________________________________________________________________________________
# Par Abdul

A_ub = -valeur_nutri
b_ub = -besoins
A_ub2 = valeur_nutri
b_ub2 = 1.1 * besoins

A_total = np.vstack((A_ub, A_ub2))
b_total = np.hstack((b_ub, b_ub2))

Result = so.linprog(prix, A_ub = -valeur_nutri, b_ub = -besoins, method = 'highs')


# Limite supérieure : 110 % des besoins
A_ub_inf = -valeur_nutri            # ≥ besoins <=> -valeurs ≤ -besoins
b_ub_inf = -besoins

# Limite supérieure : ≤ 110% des besoins
A_ub_sup = valeur_nutri
b_ub_sup = 1.1 * besoins

# Contrainte combinée
A_total = np.vstack((A_ub_inf, A_ub_sup))
b_total = np.hstack((b_ub_inf, b_ub_sup))

# Résolution avec nouvelles contraintes
Result = so.linprog(prix, A_ub=A_total, b_ub=b_total, method='highs')


# Vérification des apports réels
apports_obtenus = valeur_nutri @ Result.x  # produit matriciel
pourcentages = apports_obtenus / besoins * 100

print("\nVérification des apports nutritionnels obtenus :")
nutriments = ['Protéines', 'Lipides', 'Glucides', 'Calories', 'Fer', 'Calcium', 'Fibres']

for i in range(len(nutriments)):
    print(f"{nutriments[i]:<10} : {apports_obtenus[i]:>8.2f} ({pourcentages[i]:5.1f} % des besoins)")

# Création d'un tableau résumé avec pandas
nutriments = ['Protéines', 'Lipides', 'Glucides', 'Calories', 'Fer', 'Calcium', 'Fibres']

df_resultats = pd.DataFrame({
    'Nutriment': nutriments,
    'Besoins': besoins,
    'Apport obtenu': apports_obtenus,
    '% des besoins': pourcentages
})

# Affichage du tableau
print("\nRésumé nutritionnel :")
display(df_resultats)




# Faire en sorte que l'on puisse creer nos propres besoins _________________________________________________________________________
