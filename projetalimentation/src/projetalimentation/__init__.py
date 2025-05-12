from typing import List
from graphlib import *

class besoins(object):

    def __init__(self, nom:str, proteines:int, lipides:int, glucides:int, calories:int, fer:int, calcium, fibres:int):
        self.nom :str = nom
        self.proteines:int = proteines
        self.lipides:int = lipides
        self.glucides:int = glucides
        self.calories:int = calories
        self.fer:int = fer
        self.calcium:int = calcium
        self.fibres:int = fibres

    def __eq__(self, autre):
        return self.nom == autre.nom
    
    def __super__(self, autre):
        return self.nom > autre.nom
    
    def __sub__(self, autre):
        return self.nom < autre.nom

    def __hash__(self):
        return hash(self.nom)