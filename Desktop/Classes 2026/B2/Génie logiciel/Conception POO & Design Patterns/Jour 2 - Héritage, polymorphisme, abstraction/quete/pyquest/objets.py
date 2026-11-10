"""Les objets du jeu : armes et potions."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Arme:
    """Une arme : immuable (frozen), car une épée ne change pas en cours de partie."""

    nom: str
    degats: int
    critique: float = 0.1  # probabilité d'un coup critique (dégâts x 2)

    def __post_init__(self):
        if self.degats <= 0:
            raise ValueError("Une arme doit infliger au moins 1 point de dégâts")
        if not 0 <= self.critique <= 1:
            raise ValueError("La chance de critique doit être comprise entre 0 et 1")


@dataclass(frozen=True)
class Potion:
    """Une potion de soin."""

    nom: str
    soin: int

    def __post_init__(self):
        if self.soin <= 0:
            raise ValueError("Une potion doit soigner au moins 1 PV")


# ====================================================================== Quête 2
# TODO (étape 5) :
# - un Protocol Consommable (@runtime_checkable) : un attribut nom et une méthode utiliser(cible) -> str
# - Potion.utiliser(cible) : soigne la cible, renvoie "Brakk récupère 30 PV"
# - dataclass PotionDeMana(nom, mana) : rend du mana si la cible en a (attributs mana et mana_max),
#   sinon renvoie "<nom> n'utilise pas de mana : rien ne se passe"
# - dataclass Parchemin(nom, degats) : inflige ses dégâts à la cible,
#   renvoie "Le parchemin brûle <cible> : <degats> dégâts"
