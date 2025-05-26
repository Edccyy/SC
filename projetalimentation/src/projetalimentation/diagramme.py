import numpy as np
import matplotlib.pyplot as plt

""" 
Importation des besoins nutritionnels et des apports obtenus 
"""
from base import besoins, apports_obtenus


"""
Besoins nutritionnels de base
"""
besoins_base = {
    "Protéines" : besoins[0],
    "Lipides": besoins[1],
    "Glucides": besoins[2],
    "Calories": besoins[3],
    "Fer": besoins[4],
    "Calcium": besoins[5],
    "Fibre": besoins[6]
}

"""
Apport obtenue par le programme
"""

besoins_repondu = {
    "Protéines" : apports_obtenus[0],
    "Lipides": apports_obtenus[1],
    "Glucides": apports_obtenus[2],
    "Calories": apports_obtenus[3],
    "Fer": apports_obtenus[4],
    "Calcium": apports_obtenus[5],
    "Fibre": apports_obtenus[6]
}



"""
Diagramme de Kiviat des besoins nutritionnels et des apports obtenus
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
ax.set_title("Diagramme de Kiviat des besoins nutritionnels")
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.show()