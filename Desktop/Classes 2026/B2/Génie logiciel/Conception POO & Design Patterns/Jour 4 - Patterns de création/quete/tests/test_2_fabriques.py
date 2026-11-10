"""Étapes 2 et 3 — la fabrique de monstres (registre) et l'Abstract Factory des biomes."""
import pytest

from pyquest.config import Configuration
from pyquest.fabriques import (FabriqueDeBiome, FabriqueForet, FabriqueVolcan, creer_monstre,
                               enregistrer, generer_rencontre, types_connus)
from pyquest.objets import Consommable
from pyquest.personnages import Boss, Monstre


def test_creer_un_slime_de_niveau_2():
    slime = creer_monstre("slime", niveau=2)
    assert (slime.nom, slime.pv, slime.degats, slime.xp_donnee) == ("Slime", 25, 4, 20)


def test_le_roi_gobelin_est_un_boss():
    assert isinstance(creer_monstre("roi gobelin"), Boss)


def test_monstre_inconnu():
    with pytest.raises(ValueError):
        creer_monstre("licorne")


def test_la_difficulte_s_applique():
    Configuration().changer_difficulte("difficile")
    gobelin = creer_monstre("gobelin", niveau=1)
    assert (gobelin.pv, gobelin.degats) == (50, 8)


def test_ajouter_un_monstre_par_decorateur():
    @enregistrer("squelette")
    def _squelette(niveau):
        return Monstre("Squelette", 30, 5, 30)

    assert "squelette" in types_connus()
    assert creer_monstre("squelette").nom == "Squelette"


def test_fabrique_de_biome_abstraite():
    with pytest.raises(TypeError):
        FabriqueDeBiome()


@pytest.mark.parametrize("fabrique, nom_monstre", [(FabriqueForet(), "Loup sauvage"), (FabriqueVolcan(), "Salamandre")])
def test_rencontre_coherente(fabrique, nom_monstre):
    r = generer_rencontre(fabrique, niveau=1)
    assert r["monstre"].nom == nom_monstre
    assert isinstance(r["tresor"], Consommable)
    assert isinstance(r["lieu"], str) and r["lieu"]
