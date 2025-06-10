from IPython.display import display

from projet_a.ilfautunnom import *
from projet_a.data import Al

def ajouter_aliment(aliment : aliment) :
    """
    Ajoute un nouvel aliment au DataFrame Al.
    """
    global Al
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

    print(Al)
