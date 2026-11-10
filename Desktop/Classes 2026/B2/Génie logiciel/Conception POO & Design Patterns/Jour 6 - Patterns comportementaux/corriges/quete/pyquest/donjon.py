"""Iterator : un donjon se parcourt salle par salle avec une simple boucle for.

Les monstres sont créés À LA DEMANDE (générateur) : si le héros tombe à la
salle 2, les salles suivantes ne sont jamais générées.
"""
from .fabriques import creer_monstre


class Donjon:
    def __init__(self, fabrique, nb_salles=3, niveau=1, boss="roi gobelin"):
        if nb_salles < 1:
            raise ValueError("Un donjon a au moins une salle")
        self.fabrique = fabrique
        self.nb_salles = nb_salles
        self.niveau = niveau
        self.boss = boss

    def __iter__(self):
        for numero in range(1, self.nb_salles + 1):
            if numero == self.nb_salles:
                yield numero, creer_monstre(self.boss, self.niveau)
            else:
                yield numero, self.fabrique.creer_monstre(self.niveau)

    def __len__(self):
        return self.nb_salles
