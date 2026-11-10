"""Entraînement 2 · Le grimoire polymorphe (corrigé)

Voici une fonction écrite par un stagiaire :

    def lancer(sort, cible_pv):
        if sort["type"] == "feu":
            return cible_pv - sort["puissance"] * 2
        elif sort["type"] == "glace":
            return cible_pv - sort["puissance"]
        elif sort["type"] == "soin":
            return cible_pv + sort["puissance"]

Remplacez-la par une classe abstraite Sort(nom, puissance) avec une méthode
abstraite appliquer(pv) -> int, et trois sous-classes SortDeFeu, SortDeGlace,
SortDeSoin. Puis :
- la fonction lancer_tous(sorts, pv) applique chaque sort à la suite ;
- ajoutez un 4e sort, Poison (puissance // 2 dégâts, mais au moins 1),
  SANS modifier lancer_tous : c'est tout l'intérêt du polymorphisme.
"""
from abc import ABC, abstractmethod


class Sort(ABC):
    def __init__(self, nom, puissance):
        self.nom = nom
        self.puissance = puissance

    @abstractmethod
    def appliquer(self, pv: int) -> int:
        """Renvoie les nouveaux PV de la cible."""

    def __repr__(self):
        return f"{type(self).__name__}({self.nom!r}, {self.puissance})"


class SortDeFeu(Sort):
    def appliquer(self, pv):
        return pv - self.puissance * 2


class SortDeGlace(Sort):
    def appliquer(self, pv):
        return pv - self.puissance


class SortDeSoin(Sort):
    def appliquer(self, pv):
        return pv + self.puissance


class Poison(Sort):
    def appliquer(self, pv):
        return pv - max(1, self.puissance // 2)


def lancer_tous(sorts, pv):
    for sort in sorts:
        pv = sort.appliquer(pv)
    return pv


if __name__ == "__main__":
    grimoire = [SortDeFeu("Flammèche", 10), SortDeGlace("Givre", 5), SortDeSoin("Lumière", 8)]
    assert lancer_tous(grimoire, 100) == 83
    assert lancer_tous([Poison("Venin", 1)], 10) == 9
    assert lancer_tous([Poison("Venin", 9)] + grimoire, 100) == 79
    try:
        Sort("Abstrait", 1)
    except TypeError:
        pass
    else:
        raise AssertionError("Sort doit être abstraite")
    print("Tous les tests passent !")
