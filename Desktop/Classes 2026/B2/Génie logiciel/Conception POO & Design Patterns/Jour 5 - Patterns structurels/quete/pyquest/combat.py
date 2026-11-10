"""Combat polymorphe : n'importe quel héros contre n'importe quel monstre."""
import random

TOUR_CAPACITE = 3  # le héros utilise sa capacité spéciale tous les 3 tours


def combat(hero, monstre, rng=random, journal=None):
    if journal is None:
        journal = []
    tour = 1
    while hero.est_vivant and monstre.est_vivant:
        if tour % TOUR_CAPACITE == 0:
            # polymorphisme : on ne sait pas (et on n'a pas besoin de savoir)
            # si c'est un Guerrier, un Mage ou un Archer
            journal.append(f"Tour {tour} : " + hero.capacite_speciale(monstre, rng))
        else:
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
