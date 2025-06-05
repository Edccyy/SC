from IPython.display import display

from src.projet_a.ilfautunnom import *


def ajouter_besoins(T_besoins : besoins) -> besoins:
    """
    Ajoute de nouveaux besoins
    """
    global N_besoins
    N_besoins = besoins(
        T_besoins.proteines / T_besoins.jours,
        T_besoins.lipides / T_besoins.jours,
        T_besoins.glucides / T_besoins.jours,
        T_besoins.calories / T_besoins.jours,
        T_besoins.fer / T_besoins.jours,
        T_besoins.calcium / T_besoins.jours,
        T_besoins.fibres / T_besoins.jours,
        T_besoins.jours
    )
    print(f"Les besoins journalier sont  '{N_besoins.proteines}' g de protéines, {N_besoins.lipides}' g de lipides, '{N_besoins.glucides}' g de glucides, '{N_besoins.calories}' calories, '{N_besoins.fer}' mg de fer, '{N_besoins.calcium}' mg de calcium, '{N_besoins.fibres}' g de fibres pour {N_besoins.jours} jours.")

    return N_besoins