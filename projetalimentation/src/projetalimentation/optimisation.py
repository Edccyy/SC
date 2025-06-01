import numpy as np
import pandas as pd
import scipy.optimize as so
import matplotlib.pyplot as plt
from IPython.display import display
from __class__ import *
from data import Al, A




def optimisation() -> resultat:
    """
    Optimisation de l'alimentation en fonction des besoins nutritionnels en minimisant le coût
    """

    valeur_nutri = A[:-1]
    prix = A[-1] 

    nouveau_besoins = np.array([75, 90, 225, 2000, 9, 800, 45])  # Proteines, Lipides, Glucides, Calories, Fer, Calcium, Fibre

    Result = so.linprog(prix, A_ub = -valeur_nutri, b_ub = -nouveau_besoins, method = 'highs')


