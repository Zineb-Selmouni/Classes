"""Démo de PyQuest v1.0 — lancer avec : python -m pyquest.jeu"""
import random

from .aventure import Aventure
from .commandes import BoirePotion, Enchanter
from .enchantements import EnchantementDeFeu


def main():
    aventure = Aventure(rng=random.Random(3))
    print(aventure.nouvelle_partie("Brakk", "guerrier", "facile"))

    print("\n--- Au campement ---")
    print(aventure.agir(Enchanter(aventure.hero, EnchantementDeFeu)))
    potion = next(iter(aventure.hero.inventaire))
    print(aventure.agir(BoirePotion(aventure.hero, potion)))
    print(aventure.annuler())

    print("\n--- Le donjon de la forêt ---")
    for ligne in aventure.explorer_donjon("forêt", nb_salles=3):
        print(ligne)

    print("\nSuccès :", ", ".join(aventure.succes.debloques) or "aucun")
    print("Meilleurs scores :", aventure.terminer())


if __name__ == "__main__":
    main()
