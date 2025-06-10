from .aliments import ajouter_aliment
from .data import Al
from .ilfautunnom import *

"""
Ce fichier contient la fonction `test_nouveau_aliment`.
"""

def test_nouveau_aliment() -> aliment :
    """
    Teste l'ajout d'un nouvel aliment.
    Crée un aliment avec des valeurs prédéfinies et vérifie que l'ajout fonctionne correctement.
    Vérifie que l'objet retourné est bien un objet de type `aliment`.
    Si l'aliment existe déjà, il sera mis à jour avec les nouvelles valeurs.
    Si l'aliment n'existe pas, il sera ajouté à la liste des aliments.
    A la moindre erreur, une exception sera levée.

    Args:
        aliment (aliment): Un objet de type aliment contenant les informations nutritionnelles et le prix de l'aliment.
    """
    nom = "TestAliment"
    proteines = 10
    lipides = 5
    glucides = 20
    calories = 150
    fer = 2
    calcium = 100
    fibres = 3
    prix = 1.5

    N_aliment = ajouter_aliment(aliment(nom, proteines, lipides, glucides, calories, fer, calcium, fibres, prix))

    # Vérifications (adapte selon la structure retournée)
    assert N_aliment.nom == nom
    assert N_aliment.proteines == proteines
    assert N_aliment.lipides == lipides
    assert N_aliment.glucides == glucides
    assert N_aliment.calories == calories
    assert N_aliment.fer == fer
    assert N_aliment.calcium == calcium
    assert N_aliment.fibres == fibres
    assert N_aliment.prix == prix
    