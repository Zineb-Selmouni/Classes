"""Étape 6 — le combat polymorphe."""
import random

import pytest

from pyquest.combat import combat
from pyquest.objets import Arme
from pyquest.personnages import Archer, Boss, Guerrier, Mage, Monstre


@pytest.mark.parametrize("classe", [Guerrier, Mage, Archer])
def test_chaque_classe_bat_un_slime(classe):
    hero = classe("Héros", Arme("Arme", 10, critique=0.0))
    slime = Monstre("Slime", 40, 2, 30)
    journal = []
    assert combat(hero, slime, random.Random(0), journal) is hero
    assert journal[-1] == "Slime est vaincu ! +30 XP"


def test_capacite_speciale_au_tour_3():
    hero = Guerrier("Brakk", Arme("Hache", 5, critique=0.0))
    boss = Boss("Golem", 200, 1, 50)
    journal = []
    combat(hero, boss, random.Random(0), journal)
    assert any(ligne.startswith("Tour 3 : Brakk assène un Coup puissant") for ligne in journal)


def test_defaite():
    hero = Mage("Lyra")
    dragon = Monstre("Dragon", 1000, 60, 1000)
    assert combat(hero, dragon, random.Random(0)) is dragon
