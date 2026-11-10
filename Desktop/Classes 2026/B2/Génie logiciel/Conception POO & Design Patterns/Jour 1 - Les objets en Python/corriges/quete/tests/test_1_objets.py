"""Tests de la quête 1 — lancer avec : python -m pytest"""
import pytest

from pyquest.objets import Arme, Potion


def test_arme_valide():
    epee = Arme("Épée", 8)
    assert epee.degats == 8 and epee.critique == 0.1


def test_arme_degats_invalides():
    with pytest.raises(ValueError):
        Arme("Brindille", 0)


def test_arme_immuable():
    epee = Arme("Épée", 8)
    with pytest.raises(Exception):
        epee.degats = 99


def test_potion_invalide():
    with pytest.raises(ValueError):
        Potion("Eau", 0)
