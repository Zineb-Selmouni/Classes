"""Étape 1 · Observer : evenements.py"""
from pyquest.evenements import BusEvenements, ChasseurDeSucces, Journal
from pyquest.fabriques import creer_monstre
from pyquest.objets import Arme
from pyquest.personnages import Guerrier


def test_le_bus_appelle_les_abonnes_avec_les_donnees():
    bus, recus = BusEvenements(), []
    bus.abonner("victoire", lambda **d: recus.append(d))
    bus.publier("victoire", hero="Aria", adversaire="Slime")
    assert recus == [{"hero": "Aria", "adversaire": "Slime"}]


def test_publier_sans_abonne_ne_plante_pas():
    BusEvenements().publier("personne_n_ecoute", x=1)


def test_desabonner():
    bus, recus = BusEvenements(), []
    ecouteur = lambda **d: recus.append(d)  # noqa: E731
    bus.abonner("action", ecouteur)
    bus.desabonner("action", ecouteur)
    bus.publier("action", message="?")
    assert recus == []


def test_le_journal_ecrit_les_attaques_et_les_actions():
    bus = BusEvenements()
    journal = Journal(bus)
    hero, slime = Guerrier("Brakk"), creer_monstre("slime")
    bus.publier("attaque", auteur=hero, cible=slime, degats=7)
    bus.publier("action", message="Brakk se repose")
    assert journal.lignes == ["Brakk inflige 7 dégâts à Slime", "Brakk se repose"]


def test_les_succes_se_debloquent_une_seule_fois():
    bus = BusEvenements()
    journal, succes = Journal(bus), ChasseurDeSucces(bus)
    hero = Guerrier("Brakk", Arme("Épée", 8))
    for _ in range(3):
        bus.publier("victoire", hero=hero, adversaire=creer_monstre("slime"))
    assert succes.debloques == ["Premier sang", "Chasseur"]
    assert journal.lignes.count("*** Succès débloqué : Premier sang ***") == 1


def test_succes_tueur_de_boss_et_coup_de_maitre():
    bus = BusEvenements()
    succes = ChasseurDeSucces(bus)
    hero, roi = Guerrier("Brakk"), creer_monstre("roi gobelin")
    bus.publier("attaque", auteur=hero, cible=roi, degats=25)
    bus.publier("victoire", hero=hero, adversaire=roi)
    assert set(succes.debloques) == {"Coup de maître", "Premier sang", "Tueur de boss"}
