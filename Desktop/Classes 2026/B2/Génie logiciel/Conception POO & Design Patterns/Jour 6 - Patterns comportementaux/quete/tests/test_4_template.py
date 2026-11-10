"""Étape 4 · Template Method : rencontres.py"""
import pytest

from pyquest.etats import Empoisonne, Etourdi
from pyquest.evenements import BusEvenements, Journal
from pyquest.objets import Arme
from pyquest.personnages import Guerrier, Monstre
from pyquest.rencontres import Duel, Embuscade, Entrainement, Rencontre


class De:
    def random(self):
        return 0.9          # jamais de critique


def preparer(rencontre_cls, pv_monstre=10):
    bus = BusEvenements()
    journal = Journal(bus)
    hero = Guerrier("Brakk", Arme("Épée", 10))
    slime = Monstre("Slime", pv_monstre, 2, 30)
    return rencontre_cls(hero, slime, bus, De()), journal


def test_rencontre_est_abstraite():
    with pytest.raises(TypeError):
        Rencontre(Guerrier("Brakk"), Monstre("Slime", 10, 2, 5))


def test_un_duel_complet():
    duel, journal = preparer(Duel)
    assert duel.jouer() is duel.hero
    assert journal.lignes == ["Duel : Brakk contre Slime !", "Brakk inflige 10 dégâts à Slime",
                              "Slime est vaincu !", "+30 XP"]
    assert duel.hero.xp == 30


def test_l_embuscade_laisse_le_monstre_frapper_en_premier():
    embuscade, journal = preparer(Embuscade)
    embuscade.jouer()
    assert journal.lignes[:2] == ["Embuscade ! Slime attaque par surprise", "Slime inflige 2 dégâts à Brakk"]


def test_l_entrainement_ne_donne_pas_d_xp():
    entrainement, journal = preparer(Entrainement)
    entrainement.jouer()
    assert entrainement.hero.xp == 0
    assert journal.lignes[-1] == "Pas d'XP à l'entraînement"


def test_un_hero_etourdi_passe_son_tour_pendant_la_rencontre():
    duel, journal = preparer(Duel)
    duel.hero.etat = Etourdi()
    duel.jouer()
    assert journal.lignes[1:3] == ["Brakk est étourdi et passe son tour", "Slime inflige 2 dégâts à Brakk"]


def test_le_poison_agit_a_chaque_tour_du_personnage():
    duel, journal = preparer(Duel, pv_monstre=25)
    duel.hero.etat = Empoisonne(tours=3, degats=3)
    duel.jouer()
    assert journal.lignes.count("Brakk souffre du poison : -3 PV") == 3
