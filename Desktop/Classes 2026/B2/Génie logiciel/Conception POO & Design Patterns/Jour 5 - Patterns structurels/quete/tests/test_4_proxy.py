"""Étape 4 — Proxy : cache et protection du catalogue."""
import pytest

from pyquest.catalogue import CatalogueDistant, CatalogueEnCache, CatalogueProtege
from pyquest.personnages import Guerrier


def test_le_cache_evite_les_requetes_repetees():
    distant = CatalogueDistant()
    catalogue = CatalogueEnCache(distant)
    for _ in range(5):
        assert catalogue.fiche("slime").startswith("Masse")
    catalogue.fiche("gobelin")
    assert distant.requetes == 2


def test_le_cache_laisse_passer_les_erreurs():
    with pytest.raises(KeyError):
        CatalogueEnCache(CatalogueDistant()).fiche("licorne")


def test_fiche_secrete_refusee_a_bas_niveau():
    catalogue = CatalogueProtege(CatalogueDistant(), Guerrier("Brakk"))
    with pytest.raises(PermissionError):
        catalogue.fiche("dragon")
    assert catalogue.fiche("slime")


def test_fiche_secrete_autorisee_au_niveau_5():
    hero = Guerrier("Brakk")
    hero.gagner_xp(400)
    assert CatalogueProtege(CatalogueDistant(), hero).fiche("dragon").startswith("SECRET")


def test_les_proxys_se_combinent():
    distant = CatalogueDistant()
    hero = Guerrier("Brakk")
    catalogue = CatalogueProtege(CatalogueEnCache(distant), hero)
    catalogue.fiche("gobelin")
    catalogue.fiche("gobelin")
    assert distant.requetes == 1
