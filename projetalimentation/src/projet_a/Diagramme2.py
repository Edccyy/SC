import numpy as np
import matplotlib.pyplot as plt

from .data import *
from .aliments import ajouter_aliment
from .besoins import ajouter_besoins
from .ilfautunnom import *
from .optimisation import optimisation

"""
Ce fichier contient le code pour afficher un diagramme de Kiviat
qui compare les besoins nutritionnels et les apports obtenus par le resultat.
Il utilise directement les données transmises par l'utilisateur et les apports obtenus
"""


def plot_kiviat(N_besoins: besoins, apports_obtenus: besoins, titre: str = "Diagramme de Kiviat des besoins nutritionnels"):

    besoins_base = {
    "Protéines" : N_besoins.proteines,
    "Lipides": N_besoins.lipides,
    "Glucides": N_besoins.glucides,
    "Calories": N_besoins.calories,
    "Fer": N_besoins.fer,
    "Calcium": N_besoins.calcium,
    "Fibre": N_besoins.fibres
}

    """
    Apport obtenue par le programme
    """
    besoins_repondu = {
        "Protéines" : apports_obtenus.proteines,
        "Lipides": apports_obtenus.lipides,
        "Glucides": apports_obtenus.glucides,
        "Calories": apports_obtenus.calories,
        "Fer": apports_obtenus.fer,
        "Calcium": apports_obtenus.calcium,
        "Fibre": apports_obtenus.fibres
    }



    """
    Affiche un diagramme de Kiviat comparant les besoins de base et les apports obtenus.
    """
    labels = list(besoins_base.keys())
    n = len(labels)

    values_base = list(np.array(list(besoins_base.values())) / np.array(list(besoins_base.values())) * 100)
    values_repondu = list(np.array(list(besoins_repondu.values())) / np.array(list(besoins_base.values())) * 100)

    values_base += values_base[:1]
    values_repondu += values_repondu[:1]
    labels += labels[:1]

    angles = np.linspace(0, 2 * np.pi, n + 1, endpoint=True)

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.plot(angles, values_base, 'o-', linewidth=2, label='Besoins de base')
    ax.fill(angles, values_base, alpha=0.25)

    ax.plot(angles, values_repondu, 'o-', linewidth=2, label='Besoins répondus')
    ax.fill(angles, values_repondu, alpha=0.25)

    ax.set_thetagrids(angles * 180/np.pi, labels)
    ax.set_title(titre)
    ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

    plt.show()