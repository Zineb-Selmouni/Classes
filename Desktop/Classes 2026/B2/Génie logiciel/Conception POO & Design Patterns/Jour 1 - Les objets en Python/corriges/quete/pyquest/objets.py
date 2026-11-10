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
