"""Scénario « golden master » : une partie complète, rejouable à l'identique."""
import random


def jouer_scenario(Partie):
    random.seed(2026)
    for classe in ("guerrier", "mage", "archer"):
        p = Partie("Aria", classe)
        p.afficher()
        p.acheter("potion")
        p.acheter("epee")
        for monstre in ("slime", "gobelin", "gobelin", "orc", "slime", "orc"):
            if not p.combattre(monstre):
                break
            if p.pv < p.pv_max // 2:
                p.boire()
        p.acheter("epee")
        p.acheter("grande potion")
        p.acheter("baton magique")
        p.combattre("dragon")
        p.boire()
        p.afficher()
        print("Succès :", p.succes)
