"""Facade : une porte d'entrée simple vers tout le moteur du jeu.

Le menu du jeu (ou une future API web) n'a besoin de connaître que la classe
Aventure, pas les fabriques, le builder, le combat, la configuration, les scores…

v1.0 (jour 6) : la façade branche aussi le bus d'événements (Observer), le
journal et les succès, l'historique des commandes (Command) et les donjons (Iterator).
"""
import random

from .combat import combat
from .commandes import Historique
from .config import Configuration
from .construction import hero_de_depart
from .donjon import Donjon
from .etats import Normal
from .evenements import BusEvenements, ChasseurDeSucces, Journal
from .fabriques import FabriqueForet, FabriqueVolcan, generer_rencontre
from .rencontres import Duel, Embuscade
from .scores import TableauEnMemoire

BIOMES = {"forêt": FabriqueForet, "volcan": FabriqueVolcan}
CHANCE_EMBUSCADE = 0.25
REPOS = 0.4  # part des PV max récupérée entre deux salles


class Aventure:
    def __init__(self, tableau=None, rng=None):
        self.tableau = tableau or TableauEnMemoire()
        self.rng = rng or random.Random()
        self.hero = None
        self.score = 0
        self.bus = BusEvenements()
        self.journal = Journal(self.bus)
        self.succes = ChasseurDeSucces(self.bus)
        self.historique = Historique()
        self.bus.abonner("victoire", self._compter_points)

    def nouvelle_partie(self, nom, classe, difficulte="normal"):
        Configuration().changer_difficulte(difficulte)
        self.hero = hero_de_depart(nom, classe)
        self.score = 0
        return str(self.hero)

    def explorer(self, biome):
        """Une rencontre simple (moteur du jour 5). Renvoie le journal du combat."""
        self._verifier(biome)
        rencontre = generer_rencontre(BIOMES[biome](), self.hero.niveau)
        journal = [rencontre["lieu"]]
        vainqueur = combat(self.hero, rencontre["monstre"], self.rng, journal)
        if vainqueur is self.hero:
            self.hero.inventaire.ajouter(rencontre["tresor"])
            self.score += rencontre["monstre"].xp_donnee
            journal.append(f"Trésor : {rencontre['tresor'].nom}")
        return journal

    def explorer_donjon(self, biome, nb_salles=3):
        """Iterator + Template Method : salle après salle, jusqu'au boss ou à la défaite."""
        self._verifier(biome)
        debut = len(self.journal.lignes)
        for numero, monstre in Donjon(BIOMES[biome](), nb_salles, self.hero.niveau):
            self.bus.publier("action", message=f"--- Salle {numero}/{nb_salles} ---")
            Rencontre = Embuscade if self.rng.random() < CHANCE_EMBUSCADE else Duel
            if Rencontre(self.hero, monstre, self.bus, self.rng).jouer() is not self.hero:
                break
            self._se_reposer()
        return self.journal.lignes[debut:]

    def agir(self, commande):
        """Command : toutes les actions du campement passent par l'historique."""
        return self.historique.executer(commande)

    def annuler(self):
        return self.historique.annuler()

    def terminer(self):
        self.tableau.enregistrer(self.hero.nom, self.score)
        return self.tableau.meilleurs()

    # ------------------------------------------------------------ interne
    def _compter_points(self, hero, adversaire):
        self.score += adversaire.xp_donnee

    def _se_reposer(self):
        soin = round(self.hero.pv_max * REPOS)
        self.hero.pv += soin
        self.hero.etat = Normal()
        self.bus.publier("action", message=f"{self.hero.nom} se repose : +{soin} PV")

    def _verifier(self, biome):
        if self.hero is None:
            raise RuntimeError("Commencez une nouvelle partie")
        if biome not in BIOMES:
            raise ValueError(f"Biome inconnu : {biome}")
