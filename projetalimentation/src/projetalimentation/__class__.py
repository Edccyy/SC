from typing import List
from graphlib import *

class besoins(object):

    def __init__(self, proteines:int, lipides:int, glucides:int, calories:int, fer:int, calcium, fibres:int, jours:int, marge:int = 0):
        
        self.proteines:int = proteines*jours
        self.lipides:int = lipides*jours
        self.glucides:int = glucides*jours
        self.calories:int = calories*jours
        self.fer:int = fer*jours
        self.calcium:int = calcium*jours
        self.fibres:int = fibres*jours
        self.jours:int = jours
        self.marge:int = marge
        if marge < 0:
            raise ValueError("La marge ne peut pas être négative.")
        if marge > 100:
            raise ValueError("La marge ne peut pas être supérieure à 100%.")

    def __hash__(self):
        return hash(self.nom)
    


class aliment(object):

    def __init__(self, nom:str, proteines:int, lipides:int, glucides:int, calories:int, fer:int, calcium, fibres:int, prix:int):
        self.nom :str = nom
        self.proteines:int = proteines
        self.lipides:int = lipides
        self.glucides:int = glucides
        self.calories:int = calories
        self.fer:int = fer
        self.calcium:int = calcium
        self.fibres:int = fibres
        self.prix:int = prix


class resultat(object):

    def __init__(self, liste_aliments):
        self.liste_aliments : List[aliment] = liste_aliments
        
