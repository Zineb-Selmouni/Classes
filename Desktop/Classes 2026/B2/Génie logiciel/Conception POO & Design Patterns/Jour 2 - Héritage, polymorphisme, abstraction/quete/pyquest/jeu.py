"""Démo de PyQuest v0.1 — lancer avec : python -m pyquest.jeu"""
import random

from .combat import combat
from .objets import Arme, Potion
from .personnages import Hero, Monstre


def main():
    rng = random.Random(7)
    hero = Hero("Aria", arme=Arme("Épée courte", 8, critique=0.2))
    hero.inventaire.ajouter(Potion("Petite potion", 20))
    print(hero)
    print(hero.inventaire)
    print()

    for monstre in [Monstre("Slime", 20, 3, 40), Monstre("Gobelin", 35, 6, 70)]:
        journal = []
        vainqueur = combat(hero, monstre, rng, journal)
        print("\n".join(journal))
        if vainqueur is not hero:
            break
        if hero.pv < 50 and len(hero.inventaire) > 0:
            potion = next(iter(hero.inventaire))
            print(f"{hero.nom} boit {potion.nom} : +{hero.boire(potion)} PV")
        print(hero, "\n")


if __name__ == "__main__":
    main()
