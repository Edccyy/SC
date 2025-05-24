import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so
from IPython.display import display
from __init__ import *



np.set_printoptions(precision=1, suppress=True)




## 1)  Le problème de base___________________________________________________________________________________________________________________
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





## 2)  Les 10%___________________________________________________________________________________________________________________
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


# Création d'un tableau résumé avec pandas
nutriments = ['Protéines', 'Lipides', 'Glucides', 'Calories', 'Fer', 'Calcium', 'Fibres']

df_resultats = pd.DataFrame({
    'Nutriment': nutriments,
    'Besoins': besoins,
    'Apport obtenu': apports_obtenus,
    '% des besoins': pourcentages})




## Affichage des résultats____________________________________________________________________________________________________________________

# Affichage basique des résultats
print("")
print( "Cout : ", Result.fun)
print("")


# Affichage avancé des résultats
u = np.where(Result.x > 0)[0]  # Qté opti sup à 0

for k in u:
    print(Al.index[k])  # Nom de l'aliment
    print('{:0.2f} g'.format(Result.x[k] * 100))  # Quantité optimale en grammes

def rename_aliment(name):
    return name.replace("–", "-").strip()
# Affichage du tableau
print("\nRésumé nutritionnel :")
print(df_resultats.to_string(index=False))





# Possibilité de rajouter des aliments en utilisant la classe Aliment


def ajouter_aliment(aliment):
    """
    Ajoute un nouvel aliment au DataFrame Al.
    """
    nouvelle_ligne = [
        aliment.proteines,
        aliment.lipides,
        aliment.glucides,
        aliment.calories,
        aliment.fer,
        aliment.calcium,
        aliment.fibres,
        aliment.prix
    ]
    Al.loc[aliment.nom] = nouvelle_ligne
    print(f"Aliment '{aliment.nom}' ajouté avec succès.")