"""Étape 5 — le protocole Consommable."""
import pytest

from pyquest.objets import Arme, Consommable, Parchemin, Potion, PotionDeMana
from pyquest.personnages import Guerrier, Mage, Monstre


def test_les_consommables_respectent_le_protocole():
    for objet in (Potion("P", 10), PotionDeMana("M", 10), Parchemin("F", 10)):
        assert isinstance(objet, Consommable)
    assert not isinstance(Arme("Épée", 5), Consommable)


def test_potion_soigne_via_utiliser():
    g = Guerrier("Brakk")
    g.pv = 100
    p = Potion("Potion", 50)
    g.inventaire.ajouter(p)
    assert g.utiliser(p) == "Brakk récupère 30 PV"
    assert g.pv == 130 and p not in g.inventaire


def test_potion_de_mana():
    mage = Mage("Lyra", mana_max=60)
    mage.mana = 10
    p = PotionDeMana("Élixir", 30)
    mage.inventaire.ajouter(p)
    mage.utiliser(p)
    assert mage.mana == 40


def test_potion_de_mana_sur_un_guerrier():
    g = Guerrier("Brakk")
    p = PotionDeMana("Élixir", 30)
    g.inventaire.ajouter(p)
    assert "rien ne se passe" in g.utiliser(p)


def test_parchemin_sur_un_ennemi():
    g, m = Guerrier("Brakk"), Monstre("Slime", 40, 3, 10)
    p = Parchemin("Feu", 15)
    g.inventaire.ajouter(p)
    g.utiliser(p, m)
    assert m.pv == 25


def test_utiliser_un_objet_absent():
    with pytest.raises(ValueError):
        Guerrier("Brakk").utiliser(Potion("Potion", 10))
