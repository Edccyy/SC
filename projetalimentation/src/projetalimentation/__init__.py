from typing import List
from graphlib import *

class besoins(object):

    def __init__(self, nom:str, proteines:int, lipides:int, glucides:int, calories:int, fer:int, calcium, fibres:int, jours:int):
        self.nom :str = nom
        self.proteines:int = proteines*jours
        self.lipides:int = lipides*jours
        self.glucides:int = glucides*jours
        self.calories:int = calories*jours
        self.fer:int = fer*jours
        self.calcium:int = calcium*jours
        self.fibres:int = fibres*jours
        self.jours:int = jours

    def __eq__(self, autre):
        return self.nom == autre.nom
    
    def __super__(self, autre):
        return self.nom > autre.nom
    
    def __sub__(self, autre):
        return self.nom < autre.nom

    def __hash__(self):
        return hash(self.nom)