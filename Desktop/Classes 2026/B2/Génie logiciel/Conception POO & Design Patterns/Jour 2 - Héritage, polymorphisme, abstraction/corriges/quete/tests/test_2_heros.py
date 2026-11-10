"""Étapes 2 et 3 — Hero et les trois classes de héros."""
import pytest

from pyquest.objets import Arme
from pyquest.personnages import Archer, Guerrier, Hero, Mage, Monstre, Personnage


class FauxDe:
    def __init__(self, valeur):
        self.valeur = valeur

    def random(self):
        return self.valeur


JAMAIS_CRITIQUE = FauxDe(0.99)


def cible():
    return Monstre("Mannequin", 500, 0, 0)


def test_hero_est_abstrait():
    with pytest.raises(TypeError):
        Hero("Personne")


def test_hierarchie():
    g = Guerrier("Brakk")
    assert isinstance(g, Hero) and isinstance(g, Personnage)
    assert issubclass(Mage, Hero) and issubclass(Archer, Personnage)


def test_pv_de_depart_par_classe():
    assert Guerrier("A").pv_max == 130
    assert Mage("B").pv_max == 80
    assert Archer("C").pv_max == 100


def test_guerrier_coup_puissant():
    g, m = Guerrier("Brakk", Arme("Hache", 9)), cible()
    g.capacite_speciale(m, JAMAIS_CRITIQUE)
    assert m.pv == 500 - 18


def test_mage_boule_de_feu_consomme_du_mana():
    mage, m = Mage("Lyra", mana_max=30), cible()
    texte = mage.capacite_speciale(m, JAMAIS_CRITIQUE)
    assert m.pv == 475 and mage.mana == 10 and "Boule de feu" in texte


def test_mage_sans_mana_frappe_au_baton():
    mage, m = Mage("Lyra", Arme("Bâton", 4), mana_max=10), cible()
    texte = mage.capacite_speciale(m, JAMAIS_CRITIQUE)
    assert m.pv == 496 and "plus de mana" in texte


def test_archer_bonus_critique_avec_super():
    archer = Archer("Sylas", Arme("Arc", 7, critique=0.1))
    assert archer.chance_critique == pytest.approx(0.35)
    assert Archer("Sans arc").chance_critique == pytest.approx(0.25)


def test_archer_double_tir():
    archer, m = Archer("Sylas", Arme("Arc", 7, critique=0.0)), cible()
    archer.capacite_speciale(m, JAMAIS_CRITIQUE)
    assert m.pv == 500 - 14


def test_polymorphisme():
    equipe = [Guerrier("A"), Mage("B"), Archer("C")]
    m = cible()
    textes = [h.capacite_speciale(m, JAMAIS_CRITIQUE) for h in equipe]
    assert all(isinstance(t, str) for t in textes)


def test_str_affiche_la_classe():
    assert str(Mage("Lyra")) == "Lyra le mage (niv. 1) — PV 80/80"
