"""Étape 5 · Command : commandes.py"""
from pyquest.commandes import BoirePotion, Enchanter, EquiperArme, Historique
from pyquest.enchantements import EnchantementDeFeu
from pyquest.objets import Arme, Potion
from pyquest.personnages import Guerrier

EPEE = Arme("Épée", 8)
HACHE = Arme("Hache", 11)


def test_equiper_puis_annuler():
    hero = Guerrier("Brakk", EPEE)
    commande = EquiperArme(hero, HACHE)
    assert commande.executer() == "Brakk s'équipe : Hache"
    assert hero.arme is HACHE
    assert commande.annuler() == "Brakk reprend Épée"
    assert hero.arme is EPEE


def test_enchanter_puis_annuler():
    hero = Guerrier("Brakk", EPEE)
    commande = Enchanter(hero, EnchantementDeFeu)
    assert commande.executer() == "Arme enchantée : Épée de feu"
    assert hero.arme.degats == 12
    commande.annuler()
    assert hero.arme is EPEE


def test_annuler_une_potion_rend_les_pv_et_la_potion():
    hero, potion = Guerrier("Brakk"), Potion("Potion", 20)
    hero.inventaire.ajouter(potion)
    hero.pv = 50
    commande = BoirePotion(hero, potion)
    commande.executer()
    assert hero.pv == 70 and potion not in hero.inventaire
    assert commande.annuler() == "Potion retourne dans le sac"
    assert hero.pv == 50 and potion in hero.inventaire


def test_historique_annuler_refaire():
    hero, h = Guerrier("Brakk", EPEE), Historique()
    h.executer(EquiperArme(hero, HACHE))
    h.executer(Enchanter(hero, EnchantementDeFeu))
    assert hero.arme.nom == "Hache de feu" and len(h) == 2
    h.annuler()
    h.annuler()
    assert hero.arme is EPEE and len(h) == 0
    assert h.annuler() == "Rien à annuler"
    assert h.refaire() == "Brakk s'équipe : Hache"
    assert hero.arme is HACHE


def test_une_nouvelle_action_efface_le_refaire():
    hero, h = Guerrier("Brakk", EPEE), Historique()
    h.executer(EquiperArme(hero, HACHE))
    h.annuler()
    h.executer(Enchanter(hero, EnchantementDeFeu))
    assert h.refaire() == "Rien à refaire"
