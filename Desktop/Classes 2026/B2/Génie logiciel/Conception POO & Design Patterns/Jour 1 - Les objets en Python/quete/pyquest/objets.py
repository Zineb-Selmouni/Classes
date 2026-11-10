"""Les objets du jeu : armes et potions."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Arme:
    """Une arme : immuable (frozen), car une épée ne change pas en cours de partie.

    Exemple complet : inspirez-vous-en pour écrire Potion.
    """

    nom: str
    degats: int
    critique: float = 0.1  # probabilité d'un coup critique (dégâts x 2)

    def __post_init__(self):
        if self.degats <= 0:
            raise ValueError("Une arme doit infliger au moins 1 point de dégâts")
        if not 0 <= self.critique <= 1:
            raise ValueError("La chance de critique doit être comprise entre 0 et 1")


# TODO (étape 1) : dataclass immuable Potion(nom: str, soin: int)
# qui refuse un soin <= 0 (ValueError).
