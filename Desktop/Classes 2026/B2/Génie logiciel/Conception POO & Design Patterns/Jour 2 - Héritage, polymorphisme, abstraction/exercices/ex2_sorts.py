"""Entraînement 2 · Le grimoire polymorphe 

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


# TODO : classe abstraite Sort, puis SortDeFeu, SortDeGlace, SortDeSoin et Poison


def lancer_tous(sorts, pv):
    # TODO : une simple boucle, sans aucun if sur le type du sort !
    pass


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
