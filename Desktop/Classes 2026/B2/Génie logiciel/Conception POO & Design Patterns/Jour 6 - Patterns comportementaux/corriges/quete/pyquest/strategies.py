"""Strategy : le comportement d'un monstre en combat est un objet interchangeable.

Le monstre ne sait pas COMMENT il se bat : il délègue à sa stratégie.
On peut changer de stratégie en cours de combat, et en ajouter sans toucher Monstre.
"""
import random
from typing import Protocol

from .etats import Empoisonne, Etourdi, Normal


class StrategieDeCombat(Protocol):
    def agir(self, monstre, cible, rng) -> str: ...


class Agressive:
    def agir(self, monstre, cible, rng=random):
        degats = monstre.attaquer(cible, rng)
        return f"{monstre.nom} inflige {degats} dégâts à {cible.nom}"


class Prudente:
    """Boit ses potions quand ses PV passent sous un seuil, sinon attaque."""

    def __init__(self, seuil=0.3, soin=10, potions=1):
        self.seuil, self.soin, self.potions = seuil, soin, potions

    def agir(self, monstre, cible, rng=random):
        if self.potions > 0 and monstre.pv < self.seuil * monstre.pv_max:
            self.potions -= 1
            monstre.pv += self.soin
            return f"{monstre.nom} boit une potion : +{self.soin} PV"
        return Agressive().agir(monstre, cible, rng)


class Venimeuse:
    """Attaque, et peut empoisonner une cible en bonne santé."""

    def __init__(self, chance=0.3):
        self.chance = chance

    def agir(self, monstre, cible, rng=random):
        message = Agressive().agir(monstre, cible, rng)
        if isinstance(cible.etat, Normal) and rng.random() < self.chance:
            cible.etat = Empoisonne()
            message += " et l'empoisonne"
        return message


class Ecrasante:
    """Toutes les N attaques, un coup qui étourdit la cible."""

    def __init__(self, tous_les=3):
        self.tous_les = tous_les
        self.compteur = 0

    def agir(self, monstre, cible, rng=random):
        self.compteur += 1
        message = Agressive().agir(monstre, cible, rng)
        if self.compteur % self.tous_les == 0:
            cible.etat = Etourdi()
            message += " et l'étourdit"
        return message


class Imprevisible:
    """Composition de stratégies : en choisit une au hasard à chaque tour."""

    def __init__(self, *strategies):
        self.strategies = strategies

    def agir(self, monstre, cible, rng=random):
        return rng.choice(self.strategies).agir(monstre, cible, rng)
