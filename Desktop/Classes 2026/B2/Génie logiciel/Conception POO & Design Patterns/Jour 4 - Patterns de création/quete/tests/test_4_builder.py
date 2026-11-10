"""Étape 5 — le Builder de héros."""
import pytest

from pyquest.construction import HeroBuilder, hero_de_depart
from pyquest.objets import Arme, Potion
from pyquest.personnages import Archer, Mage


def test_construction_fluide():
    hero = (HeroBuilder().nomme("Sylas").de_classe("archer")
            .arme(Arme("Arc long", 7)).avec(Potion("Potion", 20)).au_niveau(3).construire())
    assert isinstance(hero, Archer)
    assert hero.arme.nom == "Arc long" and len(hero.inventaire) == 1 and hero.niveau == 3


def test_chaque_methode_renvoie_le_builder():
    b = HeroBuilder()
    assert b.nomme("X") is b and b.de_classe("mage") is b


def test_validation_a_la_construction():
    with pytest.raises(ValueError, match="nom"):
        HeroBuilder().de_classe("mage").construire()
    with pytest.raises(ValueError, match="classe"):
        HeroBuilder().nomme("Lyra").construire()
    with pytest.raises(ValueError):
        HeroBuilder().de_classe("barde")


def test_directeur_hero_de_depart():
    lyra = hero_de_depart("Lyra", "mage")
    assert isinstance(lyra, Mage) and lyra.arme.nom == "Bâton de chêne" and len(lyra.inventaire) == 1
