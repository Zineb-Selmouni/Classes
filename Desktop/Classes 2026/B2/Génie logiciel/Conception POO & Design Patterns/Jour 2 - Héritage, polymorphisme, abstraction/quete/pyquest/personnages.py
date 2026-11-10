"""Le héros et les monstres.

Remarque : Hero et Monstre se ressemblent beaucoup (pv, est_vivant,
recevoir_degats…). Cette duplication est volontaire : on la supprimera
au jour 2 grâce à l'héritage.
"""
import random

from .inventaire import Inventaire

XP_PAR_NIVEAU = 100
DEGATS_A_MAINS_NUES = 2


class Hero:
    nb_heros = 0  # attribut de classe : partagé par tous les héros

    def __init__(self, nom, pv_max=100, arme=None):
        self.nom = nom
        self.pv_max = pv_max
        self._pv = pv_max
        self.niveau = 1
        self.xp = 0
        self.arme = arme
        self.inventaire = Inventaire()
        Hero.nb_heros += 1

    # ---- état protégé par une propriété
    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, valeur):
        self._pv = max(0, min(valeur, self.pv_max))

    @property
    def est_vivant(self):
        return self.pv > 0

    # ---- comportement
    def degats_de_base(self):
        base = self.arme.degats if self.arme else DEGATS_A_MAINS_NUES
        return base + (self.niveau - 1)

    def attaquer(self, cible, rng=random):
        degats = self.degats_de_base()
        if self.arme and rng.random() < self.arme.critique:
            degats *= 2
        cible.recevoir_degats(degats)
        return degats

    def recevoir_degats(self, degats):
        if degats < 0:
            raise ValueError("Les dégâts ne peuvent pas être négatifs")
        self.pv -= degats

    def boire(self, potion):
        if potion not in self.inventaire:
            raise ValueError(f"{self.nom} n'a pas de {potion.nom}")
        self.inventaire.retirer(potion)
        avant = self.pv
        self.pv += potion.soin
        return self.pv - avant  # PV réellement soignés

    def gagner_xp(self, points):
        """Ajoute de l'XP. Renvoie True si le héros monte de niveau."""
        self.xp += points
        nouveau_niveau = self.xp // XP_PAR_NIVEAU + 1
        if nouveau_niveau > self.niveau:
            self.pv_max += 10 * (nouveau_niveau - self.niveau)
            self.niveau = nouveau_niveau
            self.pv = self.pv_max  # soin complet à chaque niveau
            return True
        return False

    def __str__(self):
        return f"{self.nom} (niv. {self.niveau}) — PV {self.pv}/{self.pv_max}"

    def __repr__(self):
        return f"Hero(nom={self.nom!r}, niveau={self.niveau})"


class Monstre:
    def __init__(self, nom, pv, degats, xp_donnee):
        self.nom = nom
        self.pv_max = pv
        self._pv = pv
        self.degats = degats
        self.xp_donnee = xp_donnee

    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, valeur):
        self._pv = max(0, min(valeur, self.pv_max))

    @property
    def est_vivant(self):
        return self.pv > 0

    def attaquer(self, cible, rng=random):
        cible.recevoir_degats(self.degats)
        return self.degats

    def recevoir_degats(self, degats):
        if degats < 0:
            raise ValueError("Les dégâts ne peuvent pas être négatifs")
        self.pv -= degats

    def __str__(self):
        return f"{self.nom} — PV {self.pv}/{self.pv_max}"

    def __repr__(self):
        return f"Monstre(nom={self.nom!r}, pv={self.pv})"
