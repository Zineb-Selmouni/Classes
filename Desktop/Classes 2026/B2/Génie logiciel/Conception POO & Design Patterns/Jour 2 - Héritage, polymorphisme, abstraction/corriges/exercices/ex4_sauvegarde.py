"""Entraînement 4 · Tout sauvegarder avec un Protocol (corrigé)

On veut sauvegarder des objets très différents (un héros, un coffre, une quête)
qui n'ont AUCUNE classe mère commune.
1. Définissez un Protocol Sauvegardable avec une méthode vers_dict() -> dict
   (décoré @runtime_checkable pour pouvoir utiliser isinstance).
2. Les classes Hero, Coffre et Quete (fournies sans héritage) implémentent vers_dict().
3. sauvegarder(objets) renvoie la liste des dictionnaires, en ignorant
   silencieusement les objets qui ne sont pas Sauvegardable.
"""
from typing import Protocol, runtime_checkable


@runtime_checkable
class Sauvegardable(Protocol):
    def vers_dict(self) -> dict: ...


class Hero:
    def __init__(self, nom, niveau):
        self.nom, self.niveau = nom, niveau

    def vers_dict(self):
        return {"type": "hero", "nom": self.nom, "niveau": self.niveau}


class Coffre:
    def __init__(self, contenu):
        self.contenu = list(contenu)

    def vers_dict(self):
        return {"type": "coffre", "contenu": list(self.contenu)}


class Quete:
    def __init__(self, titre, terminee=False):
        self.titre, self.terminee = titre, terminee

    def vers_dict(self):
        return {"type": "quete", "titre": self.titre, "terminee": self.terminee}


class Nuage:
    """Un décor : rien à sauvegarder."""


def sauvegarder(objets):
    return [o.vers_dict() for o in objets if isinstance(o, Sauvegardable)]


if __name__ == "__main__":
    monde = [Hero("Aria", 3), Nuage(), Coffre(["rubis"]), Quete("Le dragon", True)]
    assert sauvegarder(monde) == [
        {"type": "hero", "nom": "Aria", "niveau": 3},
        {"type": "coffre", "contenu": ["rubis"]},
        {"type": "quete", "titre": "Le dragon", "terminee": True},
    ]
    assert isinstance(Hero("A", 1), Sauvegardable)
    assert not isinstance(Nuage(), Sauvegardable)
    assert Sauvegardable not in Hero.__mro__  # aucune relation d'héritage !
    print("Tous les tests passent !")
