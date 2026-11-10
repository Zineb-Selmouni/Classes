"""Tests de la quête 1 — lancer avec : python -m pytest"""
import pytest

from pyquest.inventaire import Inventaire, InventairePleinError


class Objet:
    """Un objet minimal pour tester l'inventaire sans dépendre de Potion."""

    def __init__(self, nom):
        self.nom = nom


def test_inventaire_ajout_et_taille():
    inv = Inventaire(capacite=2)
    inv.ajouter(Objet("P1"))
    assert len(inv) == 1


def test_inventaire_plein():
    inv = Inventaire(capacite=1)
    inv.ajouter(Objet("P1"))
    with pytest.raises(InventairePleinError):
        inv.ajouter(Objet("P2"))


def test_inventaire_contient_et_retire():
    inv = Inventaire()
    p = Objet("P1")
    inv.ajouter(p)
    assert p in inv
    inv.retirer(p)
    assert p not in inv


def test_inventaire_retirer_absent():
    with pytest.raises(ValueError):
        Inventaire().retirer(Objet("Fantôme"))


def test_inventaire_str():
    inv = Inventaire()
    assert str(inv) == "Inventaire vide"
    inv.ajouter(Objet("Elixir"))
    assert str(inv) == "Inventaire : Elixir"
