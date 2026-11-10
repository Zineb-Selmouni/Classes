"""Entraînement 3 · Le piège du carré 

Pour dessiner la carte du donjon, on a une classe Rectangle avec des
propriétés largeur et hauteur modifiables. Un collègue a écrit :

    class Carre(Rectangle):      # « un carré EST un rectangle », non ?
        ...  (modifier la largeur modifie aussi la hauteur)

1. Codez Rectangle et ce Carre, puis montrez que la fonction agrandir_salle
   ci-dessous donne un résultat faux avec un Carre.
2. Corrigez la conception : Carre et Rectangle deviennent deux classes
   indépendantes qui héritent d'une classe abstraite Forme (méthode aire()).
   Un carré n'a plus de largeur/hauteur modifiables séparément.
"""


from abc import ABC, abstractmethod


def agrandir_salle(rect):
    """Double la largeur d'une salle : l'aire doit doubler."""
    aire_avant = rect.aire()
    rect.largeur = rect.largeur * 2
    return rect.aire() == aire_avant * 2


# ---------------------------------------------------- 1. la conception piégée
class RectangleNaif:
    # TODO : propriétés largeur et hauteur (avec setters) et aire()
    pass


class CarreNaif(RectangleNaif):
    # TODO : modifier la largeur modifie aussi la hauteur (et inversement)
    pass


# ---------------------------------------------------- 2. la conception corrigée
# TODO : Forme (abstraite), Rectangle, Carre


if __name__ == "__main__":
    assert agrandir_salle(RectangleNaif(3, 4)) is True
    assert agrandir_salle(CarreNaif(3)) is False  # le bug : l'aire est multipliée par 4 !
    assert agrandir_salle(Rectangle(3, 4)) is True
    salles = [Rectangle(3, 4), Carre(5)]
    assert sum(s.aire() for s in salles) == 37
    assert not isinstance(Carre(2), Rectangle)
    print("Tous les tests passent !")
