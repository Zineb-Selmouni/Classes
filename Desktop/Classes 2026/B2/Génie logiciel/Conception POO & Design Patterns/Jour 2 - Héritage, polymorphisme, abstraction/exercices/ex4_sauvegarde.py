"""Entraînement 4 · Tout sauvegarder avec un Protocol 

On veut sauvegarder des objets très différents (un héros, un coffre, une quête)
qui n'ont AUCUNE classe mère commune.
1. Définissez un Protocol Sauvegardable avec une méthode vers_dict() -> dict
   (décoré @runtime_checkable pour pouvoir utiliser isinstance).
2. Les classes Hero, Coffre et Quete (fournies sans héritage) implémentent vers_dict().
3. sauvegarder(objets) renvoie la liste des dictionnaires, en ignorant
   silencieusement les objets qui ne sont pas Sauvegardable.
"""


from typing import Protocol, runtime_checkable


# TODO : le Protocol Sauvegardable


class Hero:
    def __init__(self, nom, niveau):
        self.nom, self.niveau = nom, niveau

    # TODO : vers_dict -> {"type": "hero", "nom": ..., "niveau": ...}


class Coffre:
    def __init__(self, contenu):
        self.contenu = list(contenu)

    # TODO : vers_dict -> {"type": "coffre", "contenu": [...]}


class Quete:
    def __init__(self, titre, terminee=False):
        self.titre, self.terminee = titre, terminee

    # TODO : vers_dict -> {"type": "quete", "titre": ..., "terminee": ...}


class Nuage:
    """Un décor : rien à sauvegarder."""


def sauvegarder(objets):
    # TODO
    pass


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
