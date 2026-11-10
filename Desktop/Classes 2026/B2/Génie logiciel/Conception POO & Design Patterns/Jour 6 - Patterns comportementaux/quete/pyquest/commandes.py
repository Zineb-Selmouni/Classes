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
    """Exemple fourni : la commande mémorise ce qu'il faut pour s'annuler."""

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


# TODO : Enchanter(hero, enchantement)   (enchantement = une classe du jour 5)
#   executer -> "Arme enchantée : Épée de feu" ; annuler remet l'arme d'avant


# TODO : BoirePotion(hero, potion)
#   executer -> message de hero.utiliser(potion)
#   annuler  -> remet les PV d'avant ET la potion dans l'inventaire
#               "Potion retourne dans le sac"


class Historique:
    """L'invocateur : exécute les commandes et se souvient de l'ordre.

    executer(commande) ; annuler() ("Rien à annuler" si vide) ;
    refaire() ("Rien à refaire" si vide) ; len(historique) = commandes faites.
    Une nouvelle commande efface ce qu'on pouvait refaire.
    """

    # TODO
