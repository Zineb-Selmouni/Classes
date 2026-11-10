"""Command : chaque action du héros au campement est un objet.

On peut donc la garder dans un historique, l'annuler et la refaire.
"""
from abc import ABC, abstractmethod


class Commande(ABC):
    @abstractmethod
    def executer(self) -> str: ...

    @abstractmethod
    def annuler(self) -> str: ...


class EquiperArme(Commande):
    def __init__(self, hero, arme):
        self.hero, self.arme = hero, arme
        self._ancienne = None

    def executer(self):
        self._ancienne = self.hero.arme
        self.hero.arme = self.arme
        return f"{self.hero.nom} s'équipe : {self.arme.nom}"

    def annuler(self):
        self.hero.arme = self._ancienne
        nom = self._ancienne.nom if self._ancienne else "ses poings"
        return f"{self.hero.nom} reprend {nom}"


class Enchanter(Commande):
    """Applique un enchantement (un Decorator du jour 5) à l'arme du héros."""

    def __init__(self, hero, enchantement):
        self.hero, self.enchantement = hero, enchantement
        self._avant = None

    def executer(self):
        self._avant = self.hero.arme
        self.hero.arme = self.enchantement(self.hero.arme)
        return f"Arme enchantée : {self.hero.arme.nom}"

    def annuler(self):
        self.hero.arme = self._avant
        return f"Enchantement retiré : {self.hero.arme.nom}"


class BoirePotion(Commande):
    def __init__(self, hero, potion):
        self.hero, self.potion = hero, potion
        self._pv_avant = None

    def executer(self):
        self._pv_avant = self.hero.pv
        return self.hero.utiliser(self.potion)

    def annuler(self):
        self.hero.pv = self._pv_avant
        self.hero.inventaire.ajouter(self.potion)
        return f"{self.potion.nom} retourne dans le sac"


class Historique:
    """L'invocateur : exécute les commandes et se souvient de l'ordre."""

    def __init__(self):
        self._faites = []
        self._annulees = []

    def executer(self, commande):
        message = commande.executer()
        self._faites.append(commande)
        self._annulees.clear()          # une nouvelle action efface le « refaire »
        return message

    def annuler(self):
        if not self._faites:
            return "Rien à annuler"
        commande = self._faites.pop()
        self._annulees.append(commande)
        return commande.annuler()

    def refaire(self):
        if not self._annulees:
            return "Rien à refaire"
        commande = self._annulees.pop()
        self._faites.append(commande)
        return commande.executer()

    def __len__(self):
        return len(self._faites)
