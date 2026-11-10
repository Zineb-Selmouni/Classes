"""Tests unitaires des nouvelles classes : possibles UNIQUEMENT grâce à l'injection
de dépendances (affichage, stockage et hasard remplaçables)."""
import pytest

from moteur.affichage import AffichageMemoire
from moteur.boutique import Article, Boutique, boire
from moteur.classes import CLASSES
from moteur.combat import Combat
from moteur.hero import Hero
from moteur.monstres import BESTIAIRE, Monstre, creer_monstre
from moteur.partie import Partie
from moteur.stockage import StockageMemoire
from moteur.succes import Succes, VerificateurDeSucces


class FauxDe:
    def __init__(self, *valeurs):
        self.valeurs = list(valeurs)

    def random(self):
        return self.valeurs.pop(0) if len(self.valeurs) > 1 else self.valeurs[0]


def test_combat_sans_console_ni_hasard():
    ecran = AffichageMemoire()
    hero = Hero("Aria", CLASSES["mage"])
    assert Combat(ecran, FauxDe(0.0, 0.99)).executer(hero, Monstre("Cible", 30, 1, 0, 0)) is True
    assert ecran.messages[1] == "Tour 1 : COUP CRITIQUE ! 24 dégâts"


def test_creer_monstre_renvoie_une_copie():
    m = creer_monstre("slime")
    m.pv = 0
    assert BESTIAIRE["slime"].pv == 20


def test_ajouter_un_monstre_sans_modifier_le_code(monkeypatch):
    monkeypatch.setitem(BESTIAIRE, "liche", Monstre("Liche", 90, 15, 120, 60))
    assert creer_monstre("liche").nom == "Liche"


def test_boutique_avec_un_autre_catalogue():
    ecran = AffichageMemoire()
    hero = Hero("Aria", CLASSES["mage"])
    boutique = Boutique(ecran, {"bouclier": Article("bouclier", 15)})
    assert boutique.acheter(hero, "bouclier") is True and hero.or_ == 5


def test_boire_sans_potion():
    ecran = AffichageMemoire()
    assert boire(Hero("Aria", CLASSES["mage"]), ecran) == 0
    assert ecran.messages == ["Aucune potion !"]


def test_nouveau_succes_sans_modifier_le_verificateur():
    ecran = AffichageMemoire()
    hero = Hero("Aria", CLASSES["archer"])
    regles = [Succes("Archer d'élite", lambda h: h.classe.nom == "archer")]
    VerificateurDeSucces(ecran, regles).verifier(hero)
    assert hero.succes == ["Archer d'élite"]


def test_partie_avec_stockage_en_memoire():
    stockage, ecran = StockageMemoire(), AffichageMemoire()
    p = Partie("Aria", "guerrier", affichage=ecran, stockage=stockage, rng=FauxDe(0.99))
    p.combattre("slime")
    p.sauvegarder()
    assert stockage.donnees["xp"] == 10
    q = Partie("Bob", "mage", affichage=ecran, stockage=stockage)
    q.charger()
    assert q.nom == "Aria" and q.classe.nom == "guerrier"


def test_hero_aller_retour_en_dictionnaire():
    h = Hero("Aria", CLASSES["archer"])
    h.inventaire.append("potion")
    assert Hero.depuis_dict(h.vers_dict()).vers_dict() == h.vers_dict()
