"""Facade : une porte d'entrée simple vers tout le moteur du jeu.

Le menu du jeu (ou une future API web) n'a besoin de connaître que la classe
Aventure, pas les fabriques, le builder, le combat, la configuration, les scores…
"""
import random

from .combat import combat
from .config import Configuration
from .construction import hero_de_depart
from .fabriques import FabriqueForet, FabriqueVolcan, generer_rencontre
from .scores import TableauEnMemoire

BIOMES = {"forêt": FabriqueForet, "volcan": FabriqueVolcan}


class Aventure:
    def __init__(self, tableau=None, rng=None):
        self.tableau = tableau or TableauEnMemoire()
        self.rng = rng or random.Random()
        self.hero = None
        self.score = 0

    def nouvelle_partie(self, nom, classe, difficulte="normal"):
        Configuration().changer_difficulte(difficulte)
        self.hero = hero_de_depart(nom, classe)
        self.score = 0
        return str(self.hero)

    def explorer(self, biome):
        """Une rencontre complète : génération, combat, trésor, score. Renvoie le journal."""
        if self.hero is None:
            raise RuntimeError("Commencez une nouvelle partie")
        if biome not in BIOMES:
            raise ValueError(f"Biome inconnu : {biome}")
        rencontre = generer_rencontre(BIOMES[biome](), self.hero.niveau)
        journal = [rencontre["lieu"]]
        vainqueur = combat(self.hero, rencontre["monstre"], self.rng, journal)
        if vainqueur is self.hero:
            self.hero.inventaire.ajouter(rencontre["tresor"])
            self.score += rencontre["monstre"].xp_donnee
            journal.append(f"Trésor : {rencontre['tresor'].nom}")
        return journal

    def terminer(self):
        self.tableau.enregistrer(self.hero.nom, self.score)
        return self.tableau.meilleurs()
