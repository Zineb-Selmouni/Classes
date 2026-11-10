"""Étape 5 — un combat au tour par tour entre un héros et un monstre."""
import random


def combat(hero, monstre, rng=random, journal=None):
    """Fait combattre jusqu'à la mort d'un des deux. Renvoie le vainqueur.

    À chaque tour : le héros attaque ; si le monstre est encore en vie, il riposte.
    Chaque attaque ajoute une ligne au journal, par exemple :
        "Tour 1 : Aria inflige 8 dégâts à Slime"
    Si le héros gagne : il reçoit l'XP du monstre et la dernière ligne du journal est
        "Slime est vaincu ! +40 XP"   (suivie de "Aria passe au niveau 2 !" s'il monte)
    Sinon la dernière ligne est "Aria est tombé au combat…".
    """
    if journal is None:
        journal = []
    # TODO
