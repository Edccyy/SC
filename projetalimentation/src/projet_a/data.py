import numpy as np
import pandas as pd
from IPython.display import display

from .ilfautunnom import *

"""
Importation des données
"""


Al = pd.read_csv(
                'C:/Cours/Supply Chain/SC/projetalimentation/données/Aliments.csv', 
                sep=';', 
                index_col=0)

Al.iloc[[10*k for k in range(5)],:]


"""
Besoin de base
"""


O_besoins = np.array([75, # Proteines
                90, # Lipides
                225, # Glucides
                2000, # Calories
                9, # Fer
                800, # Calcium 
                45])# Fibre
