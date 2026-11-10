"""Entraînement 4 · Composite : le sac sans fond (corrigé)

Un sac d'aventurier peut contenir des objets… et d'autres sacs (une bourse,
un carquois…). On veut traiter un objet et un sac de la même façon.
1. Objet(nom, poids, valeur) : poids() et valeur() renvoient ses valeurs.
2. Sac(nom, poids_vide=0.5) : contient des éléments (Objet ou Sac) ;
   poids() = poids_vide + somme des poids ; valeur() = somme des valeurs.
3. inventaire(indentation=0) renvoie les lignes d'un affichage en arbre :
      Sac à dos (3.5 kg)
        Épée (2.0 kg)
        Bourse (0.6 kg)
          Rubis (0.1 kg)
"""
from abc import ABC, abstractmethod


class Element(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def poids(self) -> float: ...

    @abstractmethod
    def valeur(self) -> int: ...

    def inventaire(self, indentation=0):
        return [" " * indentation + f"{self.nom} ({round(self.poids(), 1)} kg)"]


class Objet(Element):
    def __init__(self, nom, poids, valeur):
        super().__init__(nom)
        self._poids, self._valeur = poids, valeur

    def poids(self):
        return self._poids

    def valeur(self):
        return self._valeur


class Sac(Element):
    def __init__(self, nom, poids_vide=0.5):
        super().__init__(nom)
        self.poids_vide = poids_vide
        self._contenu = []

    def ajouter(self, element):
        self._contenu.append(element)
        return self

    def poids(self):
        return self.poids_vide + sum(e.poids() for e in self._contenu)

    def valeur(self):
        return sum(e.valeur() for e in self._contenu)

    def inventaire(self, indentation=0):
        lignes = super().inventaire(indentation)
        for e in self._contenu:
            lignes += e.inventaire(indentation + 2)
        return lignes


if __name__ == "__main__":
    bourse = Sac("Bourse").ajouter(Objet("Rubis", 0.1, 50))
    sac = Sac("Sac à dos", 0.9).ajouter(Objet("Épée", 2.0, 30)).ajouter(bourse)
    assert round(sac.poids(), 1) == 3.5 and sac.valeur() == 80
    assert sac.inventaire() == ["Sac à dos (3.5 kg)", "  Épée (2.0 kg)", "  Bourse (0.6 kg)", "    Rubis (0.1 kg)"]
    print("Tous les tests passent !")
