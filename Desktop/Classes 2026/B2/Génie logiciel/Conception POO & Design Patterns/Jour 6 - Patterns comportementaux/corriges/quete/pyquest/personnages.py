"""Personnages de PyQuest v1.0.

Nouveautés du jour 6 : chaque personnage a un état (State) et chaque monstre
une stratégie de combat (Strategy).
"""
import random
from abc import ABC, abstractmethod

from .etats import Normal
from .inventaire import Inventaire
from .strategies import Agressive

XP_PAR_NIVEAU = 100
DEGATS_A_MAINS_NUES = 2


class Personnage(ABC):
    """Tout ce qui combat : héros et monstres. Classe abstraite."""

    def __init__(self, nom, pv_max):
        self.nom = nom
        self.pv_max = pv_max
        self._pv = pv_max
        self.etat = Normal()              # State : normal, empoisonné, étourdi…

    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, valeur):
        self._pv = max(0, min(valeur, self.pv_max))

    @property
    def est_vivant(self):
        return self.pv > 0

    @property
    def chance_critique(self):
        return 0.0

    @abstractmethod
    def degats_de_base(self) -> int:
        """Chaque type de personnage calcule ses dégâts à sa façon."""

    def attaquer(self, cible, rng=random):
        degats = self.degats_de_base()
        if rng.random() < self.chance_critique:
            degats *= 2
        cible.recevoir_degats(degats)
        return degats

    def recevoir_degats(self, degats):
        if degats < 0:
            raise ValueError("Les dégâts ne peuvent pas être négatifs")
        self.pv -= degats

    def __str__(self):
        return f"{self.nom} — PV {self.pv}/{self.pv_max}"

    def __repr__(self):
        return f"{type(self).__name__}(nom={self.nom!r})"


# ====================================================================== héros
class Hero(Personnage):
    """Un héros : niveau, XP, arme et inventaire. Encore abstrait :
    chaque classe de héros définit sa capacité spéciale."""

    nb_heros = 0
    PV_DE_DEPART = 100

    def __init__(self, nom, arme=None):
        super().__init__(nom, self.PV_DE_DEPART)
        self.niveau = 1
        self.xp = 0
        self.arme = arme                  # composition : le héros A une arme
        self.inventaire = Inventaire()    # composition : le héros A un inventaire
        Hero.nb_heros += 1

    def degats_de_base(self):
        base = self.arme.degats if self.arme else DEGATS_A_MAINS_NUES
        return base + (self.niveau - 1)

    @property
    def chance_critique(self):
        return self.arme.critique if self.arme else 0.0

    @abstractmethod
    def capacite_speciale(self, cible, rng=random) -> str:
        """Utilise la capacité spéciale et renvoie une phrase pour le journal."""

    def utiliser(self, objet, cible=None):
        """Utilise un consommable de l'inventaire (sur soi par défaut)."""
        self.inventaire.retirer(objet)
        return objet.utiliser(cible if cible is not None else self)

    def gagner_xp(self, points):
        self.xp += points
        nouveau_niveau = self.xp // XP_PAR_NIVEAU + 1
        if nouveau_niveau > self.niveau:
            self.pv_max += 10 * (nouveau_niveau - self.niveau)
            self.niveau = nouveau_niveau
            self.pv = self.pv_max
            return True
        return False

    def __str__(self):
        return f"{self.nom} le {type(self).__name__.lower()} (niv. {self.niveau}) — PV {self.pv}/{self.pv_max}"


class Guerrier(Hero):
    PV_DE_DEPART = 130

    def capacite_speciale(self, cible, rng=random):
        degats = self.degats_de_base() * 2
        cible.recevoir_degats(degats)
        return f"{self.nom} assène un Coup puissant : {degats} dégâts à {cible.nom}"


class Mage(Hero):
    PV_DE_DEPART = 80
    COUT_BOULE_DE_FEU = 20

    def __init__(self, nom, arme=None, mana_max=60):
        super().__init__(nom, arme)
        self.mana_max = mana_max
        self.mana = mana_max

    def capacite_speciale(self, cible, rng=random):
        if self.mana < self.COUT_BOULE_DE_FEU:
            degats = self.attaquer(cible, rng)
            return f"{self.nom} n'a plus de mana et frappe avec son bâton : {degats} dégâts"
        self.mana -= self.COUT_BOULE_DE_FEU
        degats = 25 + 5 * (self.niveau - 1)
        cible.recevoir_degats(degats)
        return f"{self.nom} lance une Boule de feu : {degats} dégâts à {cible.nom}"


class Archer(Hero):
    BONUS_CRITIQUE = 0.25

    @property
    def chance_critique(self):
        return min(1.0, super().chance_critique + self.BONUS_CRITIQUE)

    def capacite_speciale(self, cible, rng=random):
        d1 = self.attaquer(cible, rng)
        d2 = self.attaquer(cible, rng) if cible.est_vivant else 0
        return f"{self.nom} décoche un Double tir : {d1} + {d2} dégâts à {cible.nom}"


# ====================================================================== monstres
class Monstre(Personnage):
    def __init__(self, nom, pv, degats, xp_donnee, strategie=None):
        super().__init__(nom, pv)
        self.degats = degats
        self.xp_donnee = xp_donnee
        self.strategie = strategie or Agressive()   # Strategy

    def degats_de_base(self):
        return self.degats

    def agir(self, cible, rng=random):
        """Le monstre délègue sa décision à sa stratégie."""
        return self.strategie.agir(self, cible, rng)


class Boss(Monstre):
    """Un boss enragé : +50 % de dégâts sous la moitié de ses PV."""

    @property
    def enrage(self):
        return self.pv < self.pv_max / 2

    def degats_de_base(self):
        base = super().degats_de_base()
        return int(base * 1.5) if self.enrage else base

    def __str__(self):
        return super().__str__() + (" (ENRAGÉ)" if self.enrage else "")
