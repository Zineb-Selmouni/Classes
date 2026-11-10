"""Un combat au tour par tour entre un héros et un monstre."""
import random


def combat(hero, monstre, rng=random, journal=None):
    """Fait combattre jusqu'à la mort d'un des deux. Renvoie le vainqueur.

    rng : générateur aléatoire (on passe random.Random(42) dans les tests
    pour que le combat soit reproductible).
    journal : liste dans laquelle on écrit le récit du combat.
    """
    if journal is None:
        journal = []
    tour = 1
    while hero.est_vivant and monstre.est_vivant:
        degats = hero.attaquer(monstre, rng)
        journal.append(f"Tour {tour} : {hero.nom} inflige {degats} dégâts à {monstre.nom}")
        if monstre.est_vivant:
            degats = monstre.attaquer(hero, rng)
            journal.append(f"Tour {tour} : {monstre.nom} inflige {degats} dégâts à {hero.nom}")
        tour += 1
    if hero.est_vivant:
        monte = hero.gagner_xp(monstre.xp_donnee)
        journal.append(f"{monstre.nom} est vaincu ! +{monstre.xp_donnee} XP")
        if monte:
            journal.append(f"{hero.nom} passe au niveau {hero.niveau} !")
        return hero
    journal.append(f"{hero.nom} est tombé au combat…")
    return monstre
