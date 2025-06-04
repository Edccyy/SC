import numpy as np
import scipy.optimize as so
from IPython.display import display

from src.projet_a.ilfautunnom import *
from src.projet_a.data import  A, O_besoins




def optimisation(nouveau_besoins :besoins ) -> resultat:
    """
    Optimisation de l'alimentation en fonction des besoins nutritionnels en minimisant le coût
    """
    if nouveau_besoins is None:
        nouveau_besoins = O_besoins 
    valeur_nutri = A[:-1]
    prix = A[-1] 

    Result = so.linprog(prix, A_ub = -valeur_nutri, b_ub = -nouveau_besoins, method = 'highs')

