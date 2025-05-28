import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so
from IPython.display import display
from __class__ import *
from base import Al


def ajouter_aliment(Aliment: aliment) -> aliment :
    """
    Ajoute un nouvel aliment à la base de données.
    Affiche un message de succès si l'aliment est ajouté avec succès.
    """
    nouvelle_ligne = pd.Series({
        'proteines': Aliment.proteines,
        'lipides': Aliment.lipides,
        'glucides': Aliment.glucides,
        'calories': Aliment.calories,
        'fer': Aliment.fer,
        'calcium': Aliment.calcium,
        'fibres': Aliment.fibres,
        'prix': Aliment.prix
    })
    Al.loc[Aliment.nom] = nouvelle_ligne
    print(f"✅ Aliment '{Aliment.nom}' ajouté avec succès.")