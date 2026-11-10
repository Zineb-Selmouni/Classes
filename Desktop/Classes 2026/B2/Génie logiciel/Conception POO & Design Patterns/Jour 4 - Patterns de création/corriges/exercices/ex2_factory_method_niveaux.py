"""Entraînement 2 · Factory Method : les niveaux d'un jeu de plateforme (corrigé)

La classe abstraite Niveau contient l'algorithme generer(largeur) qui construit
une ligne de décor : une case sur trois est un obstacle, les autres sont du sol.
Le type d'obstacle dépend du niveau : c'est la méthode fabrique creer_obstacle().

1. Complétez Niveau.generer(largeur) : renvoie une chaîne, "_" pour le sol
   et le symbole de l'obstacle aux positions 2, 5, 8… (i % 3 == 2).
2. NiveauPrairie crée des Buisson (symbole "b"), NiveauChateau des Lave ("~").
3. Ajoutez NiveauGlace avec des Stalactite ("v") sans modifier Niveau.
"""
from abc import ABC, abstractmethod


class Obstacle(ABC):
    symbole = "?"


class Buisson(Obstacle):
    symbole = "b"


class Lave(Obstacle):
    symbole = "~"


class Stalactite(Obstacle):
    symbole = "v"


class Niveau(ABC):
    @abstractmethod
    def creer_obstacle(self) -> Obstacle:
        """La méthode fabrique."""

    def generer(self, largeur):
        cases = []
        for i in range(largeur):
            cases.append(self.creer_obstacle().symbole if i % 3 == 2 else "_")
        return "".join(cases)


class NiveauPrairie(Niveau):
    def creer_obstacle(self):
        return Buisson()


class NiveauChateau(Niveau):
    def creer_obstacle(self):
        return Lave()


class NiveauGlace(Niveau):
    def creer_obstacle(self):
        return Stalactite()


if __name__ == "__main__":
    assert NiveauPrairie().generer(9) == "__b__b__b"
    assert NiveauChateau().generer(7) == "__~__~_"
    assert NiveauGlace().generer(3) == "__v"
    try:
        Niveau()
    except TypeError:
        pass
    else:
        raise AssertionError("Niveau doit être abstraite")
    print("Tous les tests passent !")
