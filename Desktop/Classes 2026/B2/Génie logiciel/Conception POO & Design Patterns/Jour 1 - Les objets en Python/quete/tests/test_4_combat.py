"""Tests de la quête 1 — lancer avec : python -m pytest"""
import random

from pyquest.combat import combat
from pyquest.objets import Arme
from pyquest.personnages import Hero, Monstre


def test_combat_victoire():
    h = Hero("Aria", arme=Arme("Épée", 10, critique=0))
    m = Monstre("Slime", 25, 3, 40)
    journal = []
    assert combat(h, m, random.Random(1), journal) is h
    assert not m.est_vivant and h.xp == 40
    assert journal[-1] == "Slime est vaincu ! +40 XP"


def test_combat_defaite():
    h = Hero("Aria", pv_max=10)
    m = Monstre("Dragon", 500, 50, 1000)
    assert combat(h, m, random.Random(1)) is m
    assert not h.est_vivant
