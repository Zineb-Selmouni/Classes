"""Les objets du jeu : armes et consommables.

Tous les consommables respectent le protocole Consommable : ils ont un nom
et une méthode utiliser(cible) qui renvoie un message. Ils n'héritent
d'aucune classe commune : c'est du typage structurel (duck typing vérifié).
"""
from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@runtime_checkable
class Consommable(Protocol):
    nom: str

    def utiliser(self, cible) -> str: ...


@dataclass(frozen=True)
class Arme:
    nom: str
    degats: int
    critique: float = 0.1

    def __post_init__(self):
        if self.degats <= 0:
            raise ValueError("Une arme doit infliger au moins 1 point de dégâts")
        if not 0 <= self.critique <= 1:
            raise ValueError("La chance de critique doit être comprise entre 0 et 1")


@dataclass(frozen=True)
class Potion:
    nom: str
    soin: int

    def __post_init__(self):
        if self.soin <= 0:
            raise ValueError("Une potion doit soigner au moins 1 PV")

    def utiliser(self, cible):
        avant = cible.pv
        cible.pv += self.soin
        return f"{cible.nom} récupère {cible.pv - avant} PV"


@dataclass(frozen=True)
class PotionDeMana:
    nom: str
    mana: int

    def utiliser(self, cible):
        if not hasattr(cible, "mana"):
            return f"{cible.nom} n'utilise pas de mana : rien ne se passe"
        avant = cible.mana
        cible.mana = min(cible.mana_max, cible.mana + self.mana)
        return f"{cible.nom} récupère {cible.mana - avant} points de mana"


@dataclass(frozen=True)
class Parchemin:
    """Un parchemin de feu : on l'utilise sur un ennemi."""

    nom: str
    degats: int

    def utiliser(self, cible):
        cible.recevoir_degats(self.degats)
        return f"Le parchemin brûle {cible.nom} : {self.degats} dégâts"
