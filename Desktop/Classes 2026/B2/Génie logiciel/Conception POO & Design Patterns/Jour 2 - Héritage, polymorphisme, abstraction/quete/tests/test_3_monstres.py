"""Étape 4 — Monstre et Boss."""
from pyquest.personnages import Boss, Monstre, Personnage


def test_monstre_est_un_personnage():
    assert isinstance(Monstre("Slime", 20, 3, 10), Personnage)


def test_boss_herite_de_monstre():
    assert issubclass(Boss, Monstre)


def test_boss_normal_puis_enrage():
    boss = Boss("Roi Gobelin", 100, 10, 200)
    assert boss.degats_de_base() == 10 and not boss.enrage
    boss.recevoir_degats(60)
    assert boss.enrage and boss.degats_de_base() == 15
    assert str(boss) == "Roi Gobelin — PV 40/100 (ENRAGÉ)"
