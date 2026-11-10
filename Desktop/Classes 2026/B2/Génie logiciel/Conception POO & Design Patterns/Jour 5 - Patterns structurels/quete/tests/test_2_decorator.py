"""Étape 2 — Decorator : les enchantements."""
import pytest

from pyquest.enchantements import EnchantementAffute, EnchantementDeFeu, EnchantementDeGivre
from pyquest.objets import Arme
from pyquest.personnages import Guerrier, Monstre


class FauxDe:
    def __init__(self, valeur):
        self.valeur = valeur

    def random(self):
        return self.valeur


def test_un_enchantement():
    epee = EnchantementDeFeu(Arme("Épée", 8, critique=0.1))
    assert (epee.nom, epee.degats, epee.critique) == ("Épée de feu", 12, 0.1)


def test_empiler_les_enchantements():
    epee = EnchantementAffute(EnchantementDeGivre(EnchantementDeFeu(Arme("Épée", 8, critique=0.1))))
    assert epee.nom == "Épée de feu de givre affûtée"
    assert epee.degats == 14
    assert epee.critique == pytest.approx(0.25)


def test_critique_plafonne():
    arc = EnchantementAffute(EnchantementAffute(Arme("Arc", 5, critique=0.9)))
    assert arc.critique == 1.0


def test_l_arme_d_origine_n_est_pas_modifiee():
    epee = Arme("Épée", 8)
    EnchantementDeFeu(epee)
    assert epee.degats == 8 and epee.nom == "Épée"


def test_le_heros_utilise_l_arme_enchantee_sans_le_savoir():
    hero = Guerrier("Brakk", EnchantementDeFeu(Arme("Hache", 9, critique=0.0)))
    cible = Monstre("Mannequin", 100, 0, 0)
    assert hero.attaquer(cible, FauxDe(0.99)) == 13
