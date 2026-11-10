"""Étape 2 · State : etats.py (et Personnage.etat)"""
from pyquest.etats import Empoisonne, Etourdi, Normal
from pyquest.personnages import Guerrier, Monstre


def test_un_personnage_commence_dans_l_etat_normal():
    assert isinstance(Guerrier("Brakk").etat, Normal)
    assert isinstance(Monstre("Loup", 30, 5, 10).etat, Normal)
    assert Normal().debut_de_tour(Guerrier("Brakk")) == (True, None)


def test_le_poison_blesse_puis_disparait_tout_seul():
    hero = Guerrier("Brakk")
    hero.etat = Empoisonne(tours=2, degats=4)
    assert hero.etat.debut_de_tour(hero) == (True, "Brakk souffre du poison : -4 PV")
    assert isinstance(hero.etat, Empoisonne)
    hero.etat.debut_de_tour(hero)
    assert hero.pv == hero.pv_max - 8
    assert isinstance(hero.etat, Normal)                 # transition décidée par l'état


def test_un_personnage_etourdi_passe_un_seul_tour():
    hero = Guerrier("Brakk")
    hero.etat = Etourdi()
    assert hero.etat.debut_de_tour(hero) == (False, "Brakk est étourdi et passe son tour")
    assert isinstance(hero.etat, Normal)


def test_les_etats_ont_un_nom_lisible():
    assert [str(e) for e in (Normal(), Empoisonne(), Etourdi())] == ["normal", "empoisonné", "étourdi"]

