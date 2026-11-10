"""Étape 3 — Composite : les groupes de monstres."""
import random

from pyquest.combat import combat
from pyquest.groupes import GroupeDeMonstres
from pyquest.objets import Arme
from pyquest.personnages import Guerrier, Monstre


class FauxDe:
    def random(self):
        return 0.99


def bande():
    return GroupeDeMonstres("Bande", [Monstre("Gob 1", 10, 2, 5), Monstre("Gob 2", 10, 3, 5)])


def test_les_coups_frappent_le_premier_debout():
    g = bande()
    g.recevoir_degats(12)
    assert [m.pv for m in g.membres] == [0, 10]
    g.recevoir_degats(4)
    assert [m.pv for m in g.membres] == [0, 6]


def test_tous_les_vivants_attaquent():
    g, cible = bande(), Monstre("Cible", 100, 0, 0)
    assert g.attaquer(cible, FauxDe()) == 5
    g.recevoir_degats(10)
    assert g.attaquer(cible, FauxDe()) == 3


def test_vivant_xp_et_pv_agregent_les_membres():
    g = bande()
    assert g.est_vivant and g.xp_donnee == 10 and g.pv == 20
    g.recevoir_degats(10)
    g.recevoir_degats(10)
    assert not g.est_vivant


def test_groupes_imbriques():
    horde = GroupeDeMonstres("Horde", [bande(), Monstre("Chef", 30, 5, 20)])
    assert len(horde) == 3 and horde.xp_donnee == 30 and horde.pv == 50


def test_combat_fonctionne_avec_un_groupe_sans_modification():
    hero = Guerrier("Brakk", Arme("Hache", 12, critique=0.0))
    assert combat(hero, bande(), random.Random(0)) is hero
    assert hero.xp == 10


def test_str():
    g = bande()
    g.recevoir_degats(10)
    assert str(g) == "Bande (1/2 debout)"
