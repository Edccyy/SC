from typing import List
from graphlib import *

class besoins(object):

    def __init__(self, proteines:float, lipides:float, glucides:float, calories:float, fer:float, calcium:float, fibres:float, jours:int = 1, marge:int = 0):
        
        self.proteines:float = proteines*jours
        self.lipides:float = lipides*jours
        self.glucides:float = glucides*jours
        self.calories:float = calories*jours
        self.fer:float = fer*jours
        self.calcium:float = calcium*jours
        self.fibres:float = fibres*jours
        self.jours:int = jours
        self.marge:int = marge
        if marge < 0:
            raise ValueError("La marge ne peut pas être négative.")
        if marge > 100:
            raise ValueError("La marge ne peut pas être supérieure à 100%.")

    def __hash__(self):
        return hash(self.nom)
    


class aliment(object):

    def __init__(self, nom:str, proteines:float, lipides:float, glucides:float, calories:float, fer:float, calcium, fibres:float, prix:float):
        self.nom :str = nom
        self.proteines:float = proteines
        self.lipides:float = lipides
        self.glucides:float = glucides
        self.calories:float = calories
        self.fer:float = fer
        self.calcium:float = calcium
        self.fibres:float = fibres
        self.prix:float = prix


class resultat(object):

    def __init__(self, liste_aliments):
        self.liste_aliments : List[aliment] = liste_aliments
        
