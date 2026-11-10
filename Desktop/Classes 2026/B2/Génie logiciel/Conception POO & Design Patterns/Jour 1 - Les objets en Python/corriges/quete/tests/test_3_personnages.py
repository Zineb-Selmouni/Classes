"""Tests de la quête 1 — lancer avec : python -m pytest"""
import pytest

from pyquest.objets import Arme, Potion
from pyquest.personnages import Hero, Monstre


class FauxDe:
    """Faux générateur aléatoire : renvoie toujours la même valeur."""

    def __init__(self, valeur):
        self.valeur = valeur

    def random(self):
        return self.valeur


def test_pv_bornes():
    h = Hero("Aria", pv_max=50)
    h.pv = 999
    assert h.pv == 50
    h.pv = -10
    assert h.pv == 0 and not h.est_vivant


def test_attaque_sans_arme():
    h, m = Hero("Aria"), Monstre("Slime", 20, 3, 10)
    assert h.attaquer(m, FauxDe(0.9)) == 2
    assert m.pv == 18


def test_attaque_critique():
    h, m = Hero("Aria", arme=Arme("Épée", 8, critique=0.5)), Monstre("Slime", 50, 3, 10)
    assert h.attaquer(m, FauxDe(0.1)) == 16  # 0.1 < 0.5 : critique
    assert h.attaquer(m, FauxDe(0.9)) == 8


def test_degats_negatifs_refuses():
    with pytest.raises(ValueError):
        Hero("Aria").recevoir_degats(-5)


def test_boire_potion():
    h = Hero("Aria", pv_max=100)
    p = Potion("Potion", 30)
    h.inventaire.ajouter(p)
    h.pv = 90
    assert h.boire(p) == 10  # ne dépasse pas pv_max
    assert h.pv == 100 and p not in h.inventaire


def test_boire_potion_absente():
    with pytest.raises(ValueError):
        Hero("Aria").boire(Potion("Potion", 30))


def test_gagner_xp_et_niveau():
    h = Hero("Aria", pv_max=100)
    assert h.gagner_xp(50) is False
    assert h.gagner_xp(60) is True
    assert h.niveau == 2 and h.pv_max == 110 and h.pv == 110


def test_compteur_de_heros():
    avant = Hero.nb_heros
    Hero("A"), Hero("B")
    assert Hero.nb_heros == avant + 2


def test_str_et_repr():
    h = Hero("Aria")
    assert str(h) == "Aria (niv. 1) — PV 100/100"
    assert repr(h) == "Hero(nom='Aria', niveau=1)"
