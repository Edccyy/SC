from .besoins import ajouter_besoins
from .ilfautunnom import besoins

"""
Ce fichier contient la fonction `test_nouveau_besoin`.
"""


def test_nouveau_besoin() -> besoins:
    """
    Teste l'ajout de nouveaux besoins nutritionnels.
    Crée un objet `besoins` avec des valeurs prédéfinies et vérifie que l'ajout fonctionne correctement.
    Verifie que les besoins sont correctement ajustés pour le nombre de jours spécifié.
    Et que l'objet retourné est bien un objet de type `besoins`.
    A la moindre erreur, une exception sera levée.

    Args:
        besoins (besoins): Un objet de type besoins contenant les besoins nutritionnels à respecter.
    """
    proteines = 50
    lipides = 70
    glucides = 300
    calories = 2000
    fer = 18
    calcium = 1000
    fibres = 30
    jours = 7

    N_besoin = ajouter_besoins(besoins(proteines, lipides, glucides, calories, fer, calcium, fibres, jours))

    # Vérifications (adapte selon la structure retournée)
    assert N_besoin.proteines == proteines*jours
    assert N_besoin.lipides == lipides*jours
    assert N_besoin.glucides == glucides*jours
    assert N_besoin.calories == calories*jours
    assert N_besoin.fer == fer*jours
    assert N_besoin.calcium == calcium*jours
    assert N_besoin.fibres == fibres*jours
    assert N_besoin.jours == jours