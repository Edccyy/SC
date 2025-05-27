import numpy as np
import pandas as pd
import scipy.optimize as so
import matplotlib.pyplot as plt
from IPython.display import display
from __class__ import *

"""
Importation des données
"""
Al = pd.read_csv(
                'C:/Cours/Supply Chain/SC/projetalimentation/data/Aliments.csv', 
                sep=';', 
                index_col=0)

Al.iloc[[10*k for k in range(5)],:]
A = np.array(Al).T