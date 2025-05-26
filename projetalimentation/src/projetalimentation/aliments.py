import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so
from IPython.display import display
from __class__ import *
from projetalimentation.base import Al

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