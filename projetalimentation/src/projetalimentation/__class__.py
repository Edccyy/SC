from typing import List
from graphlib import *

class besoins(object):

    def __init__(self, proteines:int, lipides:int, glucides:int, calories:int, fer:int, calcium, fibres:int, jours:int):
        self.proteines:int = proteines*jours
        self.lipides:int = lipides*jours
        self.glucides:int = glucides*jours
        self.calories:int = calories*jours
        self.fer:int = fer*jours
        self.calcium:int = calcium*jours
        self.fibres:int = fibres*jours
        self.jours:int = jours

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