"""Démo de PyQuest v0.4 — lancer avec : python -m pyquest.jeu"""
import random

from .combat import combat
from .config import Configuration
from .construction import hero_de_depart
from .fabriques import FabriqueForet, FabriqueVolcan, generer_rencontre
from .salles import SalleDuTrone, SalleOrdinaire


def main():
    Configuration().changer_difficulte("facile")
    rng = random.Random(4)
    hero = hero_de_depart("Lyra", "mage")
    print(hero, "| difficulté :", Configuration().difficulte)

    for fabrique in (FabriqueForet(), FabriqueVolcan()):
        rencontre = generer_rencontre(fabrique, niveau=hero.niveau)
        print(f"\n[{fabrique.nom}] {rencontre['lieu']}")
        vainqueur = combat(hero, rencontre["monstre"], rng)
        if vainqueur is not hero:
            print(f"{hero.nom} est tombé au combat…")
            return
        hero.inventaire.ajouter(rencontre["tresor"])
        print(f"{rencontre['monstre'].nom} vaincu ! Trésor : {rencontre['tresor'].nom}")

    for salle in (SalleOrdinaire(hero.niveau), SalleDuTrone(hero.niveau)):
        texte, monstre = salle.entrer(hero)
        print("\n" + texte)
        print("Vainqueur :", combat(hero, monstre, rng).nom)
    print("\n" + str(hero))


if __name__ == "__main__":
    main()
