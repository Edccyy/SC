from .ilfautunnom import aliment
from .data import Al

""""
Ce fichier contient la fonction `ajouter_aliment`.
"""


def ajouter_aliment(aliment : aliment) :
    """
    Ajoute un nouvel aliment au DataFrame Al.

    aliment = aliment(nom, proteines, lipides, glucides, calories, fer, calcium, fibres, prix)
    ajouter_aliment(aliment)
    
    Args:
        aliment (aliment): Un objet de type aliment contenant les informations nutritionnelles et le prix de l'aliment.
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

    return(aliment)
