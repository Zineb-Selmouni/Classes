"""Étape 6 — Prototype : cloner des monstres."""
import pytest

from pyquest.prototypes import RegistreDePrototypes, registre_par_defaut


def test_cloner_renvoie_un_nouvel_objet():
    registre = registre_par_defaut()
    a, b = registre.cloner("gobelin"), registre.cloner("gobelin")
    assert a is not b and a.nom == b.nom == "Gobelin"


def test_copie_profonde():
    registre = registre_par_defaut()
    a = registre.cloner("gobelin")
    a.butin.append("rubis")
    assert registre.cloner("gobelin").butin == ["dague", "pièce"]


def test_variante_avec_modifications():
    elite = registre_par_defaut().cloner("gobelin d'élite")
    assert (elite.nom, elite.pv, elite.pv_max, elite.degats) == ("Gobelin d'élite", 60, 60, 10)


def test_prototype_inconnu():
    with pytest.raises(KeyError):
        RegistreDePrototypes().cloner("dragon")
