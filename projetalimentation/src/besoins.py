from IPython.display import display

from ilfautunnom import *

def ajouter_besoins(besoins : besoins) -> besoins:
    """
    Ajoute de nouveaux besoins
    """
    nouveaux_besoins = [
        besoins.proteines,
        besoins.lipides,
        besoins.glucides,
        besoins.calories,
        besoins.fer,
        besoins.calcium,
        besoins.fibres,
        besoins.jours
    ]
    print(f"Les besoins journalier sont  '{besoins.proteines}' g de protéines, {besoins.lipides}' g de lipides, '{besoins.glucides}' g de glucides, '{besoins.calories}' calories, '{besoins.fer}' mg de fer, '{besoins.calcium}' mg de calcium, '{besoins.fibres}' g de fibres pour {besoins.jours} jours.")
