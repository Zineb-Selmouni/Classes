"""Le héros et les monstres (étapes 3 et 4)."""
import random

from .inventaire import Inventaire

XP_PAR_NIVEAU = 100
DEGATS_A_MAINS_NUES = 2


class Hero:
    nb_heros = 0  # attribut de classe : compte tous les héros créés

    def __init__(self, nom, pv_max=100, arme=None):
        self.nom = nom
        self.pv_max = pv_max
        self._pv = pv_max
        self.niveau = 1
        self.xp = 0
        self.arme = arme
        self.inventaire = Inventaire()
        Hero.nb_heros += 1

    # TODO : propriété pv (lecture) + setter qui borne entre 0 et pv_max

    # TODO : propriété est_vivant

    def degats_de_base(self):
        """Dégâts de l'arme (ou 2 à mains nues) + (niveau - 1)."""
        # TODO

    def attaquer(self, cible, rng=random):
        """Inflige les dégâts de base à la cible, doublés si rng.random() < arme.critique.
        Renvoie les dégâts infligés."""
        # TODO

    def recevoir_degats(self, degats):
        """Retire des PV. Dégâts négatifs -> ValueError."""
        # TODO

    def boire(self, potion):
        """La potion doit être dans l'inventaire (sinon ValueError) ; on la retire,
        on soigne sans dépasser pv_max, et on renvoie les PV réellement soignés."""
        # TODO

    def gagner_xp(self, points):
        """Ajoute l'XP. Niveau = xp // 100 + 1. À chaque niveau gagné : pv_max += 10
        et soin complet. Renvoie True si le héros a monté de niveau."""
        # TODO

    # TODO : __str__ -> "Aria (niv. 1) — PV 100/100"
    #        __repr__ -> "Hero(nom='Aria', niveau=1)"


class Monstre:
    """Étape 4 — Monstre(nom, pv, degats, xp_donnee)

    Mêmes règles de PV que le héros. attaquer(cible, rng) inflige toujours
    self.degats et les renvoie. __str__ -> "Slime — PV 20/20".
    """

    # TODO
