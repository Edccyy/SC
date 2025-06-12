from typing import List

"""
fichier contenant les classes pour les besoins, les aliments et les résultats.
"""


class besoins(object):
    """
    Classe représentant les besoins nutritionnels d'une personne ainsi que la durée.
    args:
        proteines (float): Besoin en protéines en grammes.
        lipides (float): Besoin en lipides en grammes.
        glucides (float): Besoin en glucides en grammes.
        calories (float): Besoin en calories.
        fer (float): Besoin en fer en milligrammes.
        calcium (float): Besoin en calcium en milligrammes.
        fibres (float): Besoin en fibres en grammes.
        jours (int): Nombre de jours pour lesquels les besoins sont calculés.
        marge (int): Marge de dépacement en pourcentage (0-100).
        """
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
    """
    Classe représentant un aliment avec ses valeurs nutritionnelles et son prix.
    args:
        nom (str): Nom de l'aliment.
        proteines (float): Quantité de protéines en grammes.
        lipides (float): Quantité de lipides en grammes.
        glucides (float): Quantité de glucides en grammes.
        calories (float): Quantité de calories.
        fer (float): Quantité de fer en milligrammes.
        calcium (float): Quantité de calcium en milligrammes.
        fibres (float): Quantité de fibres en grammes.
        prix (float): Prix de l'aliment.
    """
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
    """
    Classe représentant le résultat de l'optimisation des apports nutritionnels.
    args:
        liste_aliments (List[aliment]): Liste des aliments sélectionnés pour répondre aux besoins.
    """
    def __init__(self, liste_aliments):
        self.liste_aliments : List[aliment] = liste_aliments
        
