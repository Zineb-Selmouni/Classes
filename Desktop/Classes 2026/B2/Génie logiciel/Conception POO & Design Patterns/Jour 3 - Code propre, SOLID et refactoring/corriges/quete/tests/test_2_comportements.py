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


def test_monstre_inconnu():
    with pytest.raises(ValueError, match="monstre inconnu : licorne"):
        Partie("Aria", "mage").creer_monstre("licorne")


def test_victoire_rapporte_xp_or_et_succes(jamais_critique, capsys):
    p = Partie("Aria", "mage")
    assert p.combattre("slime") is True
    assert (p.xp, p.or_, p.monstres_tues) == (10, 25, 1)
    assert p.succes == ["Premier sang"]
    assert "Succès débloqué : Premier sang" in capsys.readouterr().out


def test_armure_du_guerrier(jamais_critique, capsys):
    p = Partie("Aria", "guerrier")
    p.combattre("gobelin")
    assert "Gobelin inflige 4 dégâts" in capsys.readouterr().out  # 6 - 2 d'armure


def test_defaite_contre_le_dragon(jamais_critique):
    p = Partie("Aria", "mage")
    assert p.combattre("dragon") is False
    assert p.pv == 0


def test_montee_de_niveau(jamais_critique):
    p = Partie("Aria", "guerrier")
    for _ in range(4):
        p.combattre("orc")
    assert p.niveau == 3 and "Vétéran" in p.succes


def test_reduction_de_l_archer():
    p = Partie("Aria", "archer")
    assert p.acheter("potion") is True
    assert p.or_ == 12  # 20 - (10 - 2)


def test_objet_inconnu_et_pas_assez_d_or(capsys):
    p = Partie("Aria", "mage")
    assert p.acheter("baton magique") is False
    assert p.acheter("epee") is False
    sortie = capsys.readouterr().out
    assert "Objet inconnu" in sortie and "Pas assez d'or !" in sortie


def etat(partie):
    """L'objet qui porte l'état du héros : la Partie elle-même avant le refactoring,
    partie.hero après. Les tests restent valables dans les deux cas."""
    return getattr(partie, "hero", partie)


def test_l_epee_augmente_l_attaque():
    p = Partie("Aria", "mage")
    etat(p).or_ = 100
    p.acheter("epee")
    assert p.attaque == 17


def test_boire_prend_la_plus_grande_potion():
    p = Partie("Aria", "guerrier")
    etat(p).inventaire += ["potion", "grande potion"]
    etat(p).pv = 10
    assert p.boire() == 50
    assert p.inventaire == ["potion"]


def test_sauvegarde_puis_chargement(jamais_critique):
    p = Partie("Aria", "archer")
    p.combattre("orc")
    p.sauvegarder()
    q = Partie("Bob", "mage")
    q.charger()
    assert (q.nom, q.niveau, q.xp, q.or_, q.succes) == ("Aria", 1, 50, 50, ["Premier sang"])
