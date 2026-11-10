"""Composite : un groupe de monstres se combat exactement comme un seul monstre.

Le groupe peut contenir des monstres… ou d'autres groupes (une escouade dans une horde).
La fonction combat() n'a pas besoin d'être modifiée.
"""
import random

from .etats import Normal


class GroupeDeMonstres:
    def __init__(self, nom, membres=()):
        self.nom = nom
        self._membres = list(membres)
        self.etat = Normal()

    def ajouter(self, membre):
        self._membres.append(membre)

    @property
    def membres(self):
        return list(self._membres)

    @property
    def est_vivant(self):
        return any(m.est_vivant for m in self._membres)

    @property
    def pv(self):
        return sum(m.pv for m in self._membres)

    @property
    def xp_donnee(self):
        return sum(m.xp_donnee for m in self._membres)

    def recevoir_degats(self, degats):
        """Les coups frappent le premier membre encore debout."""
        for m in self._membres:
            if m.est_vivant:
                m.recevoir_degats(degats)
                return

    def attaquer(self, cible, rng=random):
        """Chaque membre vivant attaque ; renvoie le total des dégâts."""
        return sum(m.attaquer(cible, rng) for m in self._membres if m.est_vivant)

    def agir(self, cible, rng=random):
        """Jour 6 : chaque membre vivant agit selon SA stratégie."""
        return " / ".join(m.agir(cible, rng) for m in self._membres if m.est_vivant and cible.est_vivant)

    def __len__(self):
        return sum(len(m) if isinstance(m, GroupeDeMonstres) else 1 for m in self._membres)

    def __str__(self):
        vivants = sum(1 for m in self._membres if m.est_vivant)
        return f"{self.nom} ({vivants}/{len(self._membres)} debout)"
