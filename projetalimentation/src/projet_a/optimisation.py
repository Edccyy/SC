import numpy as np
import pandas as pd
import scipy.optimize as so
from IPython.display import display

from src.projet_a.ilfautunnom import *
from src.projet_a.data import  Al, A, O_besoins



def optimisation(nouveau_besoins : besoins ) -> resultat:
    """
    Optimisation de l'alimentation en fonction des besoins nutritionnels en minimisant le coût
    """
    if nouveau_besoins is None:
        besoins_opti = O_besoins
    else:
        besoins_opti = np.array([
            nouveau_besoins.proteines,
            nouveau_besoins.lipides,
            nouveau_besoins.glucides,
            nouveau_besoins.calories,
            nouveau_besoins.fer,
            nouveau_besoins.calcium,
            nouveau_besoins.fibres
        ])
    valeur_nutri = A[:-1]
    prix = A[-1] 
    print(besoins_opti)
    Result = so.linprog(prix, A_ub = -valeur_nutri, b_ub = -besoins_opti, method = 'highs')

        # Vérification des apports réels
    apports_obtenus = valeur_nutri @ Result.x  # produit matriciel
    pourcentages = apports_obtenus / besoins_opti * 100



    """
    Tableau des résultats
    """
    nutriments = ['Protéines', 'Lipides', 'Glucides', 'Calories', 'Fer', 'Calcium', 'Fibres']

    df_resultats = pd.DataFrame({
        'Nutriment': nutriments,
        'Besoins': besoins_opti,
        'Apport obtenu': apports_obtenus,
        '% des besoins': pourcentages})




    ## Affichage des résultats____________________________________________________________________________________________________________________

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
