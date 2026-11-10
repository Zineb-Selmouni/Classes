"""Étape 4 — Factory Method : les salles."""
import pytest

from pyquest.personnages import Boss, Guerrier
from pyquest.salles import Salle, SalleDuTrone, SalleOrdinaire


def test_salle_est_abstraite():
    with pytest.raises(TypeError):
        Salle()


def test_salle_ordinaire_selon_le_niveau():
    assert SalleOrdinaire(1).creer_monstre().nom == "Slime"
    assert SalleOrdinaire(3).creer_monstre().nom == "Gobelin"


def test_salle_du_trone():
    texte, monstre = SalleDuTrone(2).entrer(Guerrier("Brakk"))
    assert isinstance(monstre, Boss)
    assert texte == "Brakk entre dans la salle du trône : un Roi Gobelin surgit !"
