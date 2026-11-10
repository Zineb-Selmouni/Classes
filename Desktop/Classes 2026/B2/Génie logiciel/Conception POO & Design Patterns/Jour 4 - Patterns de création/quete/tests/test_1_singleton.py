"""Étape 1 — la Configuration est un Singleton."""
import pytest

from pyquest.config import Configuration


def test_toujours_la_meme_instance():
    assert Configuration() is Configuration()


def test_l_etat_est_partage():
    Configuration().changer_difficulte("difficile")
    assert Configuration().difficulte == "difficile"
    assert Configuration().multiplicateur == 1.5


def test_difficulte_inconnue():
    with pytest.raises(ValueError):
        Configuration().changer_difficulte("cauchemar")


def test_reinitialiser():
    Configuration().changer_difficulte("facile")
    Configuration.reinitialiser()
    assert Configuration().difficulte == "normal"
