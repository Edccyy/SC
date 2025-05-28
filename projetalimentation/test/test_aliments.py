import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from aliments import ajouter_aliment
from data import Al
from __class__ import *


def test_nouveau_aliment() -> aliment :
    nom = "TestAliment"
    proteines = 10
    lipides = 5
    glucides = 20
    calories = 150
    fer = 2
    calcium = 100
    fibres = 3
    prix = 1.5

    N_aliment = ajouter_aliment(aliment(nom, proteines, lipides, glucides, calories, fer, calcium, fibres, prix))

    # Vérifications (adapte selon la structure retournée)
    assert N_aliment.nom == nom
    assert N_aliment.proteines == proteines
    assert N_aliment.lipides == lipides
    assert N_aliment.glucides == glucides
    assert N_aliment.calories == calories
    assert N_aliment.fer == fer
    assert N_aliment.calcium == calcium
    assert N_aliment.fibres == fibres
    assert N_aliment.prix == prix