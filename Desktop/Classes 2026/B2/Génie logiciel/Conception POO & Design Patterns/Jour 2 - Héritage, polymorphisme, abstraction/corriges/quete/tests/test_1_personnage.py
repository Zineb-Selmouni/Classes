"""Étape 1 — la classe abstraite Personnage."""
import pytest

from pyquest.personnages import Personnage


class Mannequin(Personnage):
    """Le plus petit personnage concret possible, pour tester la classe de base."""

    def degats_de_base(self):
        return 5


def test_personnage_est_abstrait():
    with pytest.raises(TypeError):
        Personnage("Personne", 10)


def test_sous_classe_sans_degats_de_base_reste_abstraite():
    class Incomplet(Personnage):
        pass

    with pytest.raises(TypeError):
        Incomplet("X", 10)


def test_pv_bornes():
    m = Mannequin("Mannequin", 50)
    m.pv = 999
    assert m.pv == 50
    m.recevoir_degats(80)
    assert m.pv == 0 and not m.est_vivant


def test_attaquer_utilise_degats_de_base():
    a, b = Mannequin("A", 50), Mannequin("B", 50)
    assert a.attaquer(b) == 5 and b.pv == 45


def test_repr_utilise_le_vrai_type():
    assert repr(Mannequin("Bob", 10)) == "Mannequin(nom='Bob')"
