"""Démo de PyQuest v0.5 — lancer avec : python -m pyquest.jeu"""
import random

from .aventure import Aventure
from .combat import combat
from .enchantements import EnchantementAffute, EnchantementDeFeu
from .fabriques import creer_monstre
from .groupes import GroupeDeMonstres
from .scores import AdaptateurArcadeCloud, ArcadeCloudAPI


def main():
    aventure = Aventure(AdaptateurArcadeCloud(ArcadeCloudAPI()), random.Random(5))
    print(aventure.nouvelle_partie("Brakk", "guerrier", "facile"))

    hero = aventure.hero
    hero.arme = EnchantementAffute(EnchantementDeFeu(hero.arme))
    print(f"Arme enchantée : {hero.arme.nom} ({hero.arme.degats} dégâts, {hero.arme.critique:.0%} de critique)")

    for biome in ("forêt", "volcan"):
        print(f"\n--- {biome} ---")
        print("\n".join(aventure.explorer(biome)[-3:]))

    horde = GroupeDeMonstres("Bande de gobelins", [creer_monstre("gobelin"), creer_monstre("gobelin")])
    print(f"\n--- {horde} ---")
    vainqueur = combat(hero, horde, random.Random(1))
    print(f"Vainqueur : {vainqueur.nom} | {horde}")

    print("\nMeilleurs scores :", aventure.terminer())


if __name__ == "__main__":
    main()
