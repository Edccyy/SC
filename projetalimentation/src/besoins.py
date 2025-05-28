import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so
from IPython.display import display
from __class__ import *


"""
def ajouter_besoin(besoins):
    

    nouveaux_besoins = [
        besoins.proteines,
        besoins.lipides,
        besoins.glucides,
        besoins.calories,
        besoins.fer,
        besoins.calcium,
        besoins.fibres,
        besoins.jours
    ]
"""

def ajouter_besoins(Besoins: besoins) -> besoins :
    """
    Ajoute un nouvel aliment à la base de données.
    Affiche un message de succès si l'aliment est ajouté avec succès.
    """
    N_besoins = [
        Besoins.proteines* Besoins.jours,
        Besoins.lipides* Besoins.jours,
        Besoins.glucides* Besoins.jours,
        Besoins.calories* Besoins.jours,
        Besoins.fer* Besoins.jours,
        Besoins.calcium* Besoins.jours,
        Besoins.fibres* Besoins.jours,
        Besoins.jours
    ]

    print(f"Les besoins journalier sont  '{Besoins.proteines}' g de protéines, {Besoins.lipides}' g de lipides, '{Besoins.glucides}' g de glucides, '{Besoins.calories}' calories, '{Besoins.fer}' mg de fer, '{Besoins.calcium}' mg de calcium, '{Besoins.fibres}' g de fibres pour {Besoins.jours} jours.")