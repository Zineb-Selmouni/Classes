"""Tests de caractérisation : ils décrivent ce que fait le code AUJOURD'HUI,
bugs compris. Ils doivent passer avant et après le refactoring."""
import random

import pytest

from moteur import Partie


@pytest.fixture(autouse=True)
def dossier_temporaire(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)  # la sauvegarde s'écrit dans un dossier jetable


@pytest.fixture
def jamais_critique(monkeypatch):
    monkeypatch.setattr(random, "random", lambda: 0.99)


def test_classe_inconnue():
    with pytest.raises(ValueError, match="classe inconnue : voleur"):
        Partie("Aria", "voleur")


@pytest.mark.parametrize("classe, pv, attaque", [("guerrier", 130, 9), ("mage", 80, 12), ("archer", 100, 8)])
def test_statistiques_de_depart(classe, pv, attaque):
    p = Partie("Aria", classe)
    assert (p.pv, p.pv_max, p.attaque, p.niveau, p.xp, p.or_) == (pv, pv, attaque, 1, 0, 20)


# TODO (étape 1) : écrivez les tests de caractérisation qui manquent, AVANT de toucher au code.
# Ils doivent passer sur l'ancienne Partie (legacy.py). Idées de comportements à figer :
#   - un monstre inconnu lève ValueError("monstre inconnu : …")
#   - une victoire donne l'XP, l'or, incrémente monstres_tues et débloque « Premier sang »
#   - le guerrier subit 2 dégâts de moins (armure)
#   - perdre contre le dragon : combattre renvoie False et les PV tombent à 0
#   - monter de niveau (4 orcs pour le guerrier) et débloquer « Vétéran »
#   - l'archer paie 2 pièces de moins ; objet inconnu ; pas assez d'or
#   - l'épée ajoute 5 d'attaque ; boire choisit la grande potion d'abord
#   - sauvegarder puis charger restaure toute la partie
