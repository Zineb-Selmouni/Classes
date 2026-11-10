"""Démo de PyQuest v0.2 — lancer avec : python -m pyquest.jeu"""
import random

from .combat import combat
from .objets import Arme, Parchemin, Potion
from .personnages import Archer, Boss, Guerrier, Mage


def main():
    rng = random.Random(3)
    equipe = [Guerrier("Brakk", Arme("Hache", 9)), Mage("Lyra", Arme("Bâton", 4)), Archer("Sylas", Arme("Arc long", 7, critique=0.15))]
    for hero in equipe:
        hero.inventaire.ajouter(Potion("Petite potion", 25))
        hero.inventaire.ajouter(Parchemin("Parchemin de feu", 15))

    for hero in equipe:  # polymorphisme : la même boucle pour les trois classes
        boss = Boss("Roi Gobelin", 90, 8, 120)
        print(f"=== {hero} contre le {boss.nom}")
        journal = []
        parchemin = next(o for o in hero.inventaire if isinstance(o, Parchemin))
        journal.append(hero.utiliser(parchemin, boss))
        vainqueur = combat(hero, boss, rng, journal)
        print("\n".join(journal))
        print(f"Vainqueur : {vainqueur.nom}\n")


if __name__ == "__main__":
    main()
