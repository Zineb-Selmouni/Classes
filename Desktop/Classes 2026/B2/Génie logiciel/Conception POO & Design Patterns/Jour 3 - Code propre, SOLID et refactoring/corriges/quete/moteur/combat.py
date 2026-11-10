"""Le combat, avec ses dépendances injectées (hasard et affichage)."""
import random


class Combat:
    def __init__(self, affichage, rng=random):
        self.affichage = affichage
        self.rng = rng

    def executer(self, hero, monstre):
        """Combat jusqu'à la mort d'un des deux. Renvoie True si le héros gagne."""
        dire = self.affichage.afficher
        dire(f"=== Combat : {hero.nom} contre {monstre.nom} ===")
        tour = 1
        while hero.est_vivant and monstre.est_vivant:
            degats = hero.degats()
            if self.rng.random() < hero.crit:
                degats *= 2
                dire(f"Tour {tour} : COUP CRITIQUE ! {degats} dégâts")
            else:
                dire(f"Tour {tour} : {hero.nom} inflige {degats} dégâts")
            monstre.pv -= degats
            if not monstre.est_vivant:
                break
            subis = hero.subir(monstre.attaque)
            dire(f"Tour {tour} : {monstre.nom} inflige {subis} dégâts")
            tour += 1
        if not hero.est_vivant:
            dire(f"{hero.nom} est mort...")
            return False
        dire(f"{monstre.nom} est vaincu !")
        for niveau in hero.recompenser(monstre):
            dire(f"{hero.nom} passe au niveau {niveau} !")
        return True
