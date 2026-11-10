"""Étape 5 — Facade : l'Aventure."""
import random

import pytest

from pyquest.aventure import Aventure
from pyquest.config import Configuration
from pyquest.scores import TableauEnMemoire


def test_nouvelle_partie_configure_tout():
    a = Aventure(rng=random.Random(0))
    texte = a.nouvelle_partie("Lyra", "mage", "difficile")
    assert texte.startswith("Lyra le mage") and Configuration().difficulte == "difficile"
    assert len(a.hero.inventaire) == 1


def test_explorer_sans_partie():
    with pytest.raises(RuntimeError):
        Aventure().explorer("forêt")


def test_biome_inconnu():
    a = Aventure()
    a.nouvelle_partie("Brakk", "guerrier")
    with pytest.raises(ValueError):
        a.explorer("océan")


def test_explorer_puis_terminer():
    tableau = TableauEnMemoire()
    a = Aventure(tableau, random.Random(0))
    a.nouvelle_partie("Brakk", "guerrier", "facile")
    journal = a.explorer("forêt")
    assert journal[0].startswith("Une clairière")
    assert journal[-1] == "Trésor : Sève de chêne"
    assert a.terminer() == [("Brakk", a.score)] and a.score > 0
