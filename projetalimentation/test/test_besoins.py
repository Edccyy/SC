import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from besoins import ajouter_besoins
from data import Al
from __class__ import *

def test_nouveau_besoin() -> besoins:
    proteines = 50
    lipides = 70
    glucides = 300
    calories = 2000
    fer = 18
    calcium = 1000
    fibres = 30
    jours = 7

    N_besoin = ajouter_besoins(besoins(proteines, lipides, glucides, calories, fer, calcium, fibres, jours))

    # Vérifications (adapte selon la structure retournée)
    assert N_besoin.proteines == proteines*jours
    assert N_besoin.lipides == lipides*jours
    assert N_besoin.glucides == glucides*jours
    assert N_besoin.calories == calories*jours
    assert N_besoin.fer == fer*jours
    assert N_besoin.calcium == calcium*jours
    assert N_besoin.fibres == fibres*jours
    assert N_besoin.jours == jours