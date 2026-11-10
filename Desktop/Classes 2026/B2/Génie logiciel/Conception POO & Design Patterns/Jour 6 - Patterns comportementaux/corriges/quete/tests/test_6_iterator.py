"""Étape 6 · Iterator : donjon.py, puis Aventure v1.0"""
import random

import pytest

from pyquest.aventure import Aventure
from pyquest.donjon import Donjon
from pyquest.fabriques import FabriqueForet
from pyquest.personnages import Boss


class FabriqueQuiCompte(FabriqueForet):
    def __init__(self):
        self.appels = 0

    def creer_monstre(self, niveau):
        self.appels += 1
        return super().creer_monstre(niveau)


def test_un_donjon_se_parcourt_avec_for_et_finit_par_un_boss():
    salles = list(Donjon(FabriqueForet(), nb_salles=4))
    assert [numero for numero, _ in salles] == [1, 2, 3, 4]
    assert isinstance(salles[-1][1], Boss)
    assert not isinstance(salles[0][1], Boss)
    assert len(Donjon(FabriqueForet(), nb_salles=4)) == 4


def test_les_salles_sont_generees_a_la_demande():
    fabrique = FabriqueQuiCompte()
    donjon = Donjon(fabrique, nb_salles=10)
    assert fabrique.appels == 0                       # rien n'est créé d'avance
    for numero, _ in donjon:
        if numero == 2:
            break
    assert fabrique.appels == 2


def test_on_peut_parcourir_un_donjon_plusieurs_fois():
    donjon = Donjon(FabriqueForet(), nb_salles=2)
    assert len(list(donjon)) == len(list(donjon)) == 2


def test_un_donjon_vide_est_refuse():
    with pytest.raises(ValueError):
        Donjon(FabriqueForet(), nb_salles=0)


def test_aventure_explorer_donjon():
    aventure = Aventure(rng=random.Random(3))
    aventure.nouvelle_partie("Brakk", "guerrier", "facile")
    lignes = aventure.explorer_donjon("forêt", nb_salles=3)
    assert lignes[0] == "--- Salle 1/3 ---"
    assert "*** Succès débloqué : Premier sang ***" in lignes
    assert aventure.score > 0                          # compté par un observateur


def test_aventure_commandes_annulables():
    from pyquest.commandes import Enchanter
    from pyquest.enchantements import EnchantementDeFeu
    aventure = Aventure(rng=random.Random(1))
    aventure.nouvelle_partie("Aria", "archer")
    arme = aventure.hero.arme
    aventure.agir(Enchanter(aventure.hero, EnchantementDeFeu))
    assert aventure.hero.arme.nom.endswith("de feu")
    aventure.annuler()
    assert aventure.hero.arme is arme
