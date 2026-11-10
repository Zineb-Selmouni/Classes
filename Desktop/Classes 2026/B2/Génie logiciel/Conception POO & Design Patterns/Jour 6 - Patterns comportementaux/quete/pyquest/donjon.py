"""Iterator : un donjon se parcourt salle par salle avec une simple boucle for.

    for numero, monstre in Donjon(FabriqueForet(), nb_salles=3):
        ...

Les monstres sont créés À LA DEMANDE (générateur) : si le héros tombe à la
salle 2, les salles suivantes ne sont jamais générées.
La dernière salle contient le boss : creer_monstre(boss, niveau).
"""
from .fabriques import creer_monstre  # noqa: F401


class Donjon:
    def __init__(self, fabrique, nb_salles=3, niveau=1, boss="roi gobelin"):
        # TODO : ValueError si nb_salles < 1
        pass

    # TODO : __iter__ (un générateur avec yield) et __len__
