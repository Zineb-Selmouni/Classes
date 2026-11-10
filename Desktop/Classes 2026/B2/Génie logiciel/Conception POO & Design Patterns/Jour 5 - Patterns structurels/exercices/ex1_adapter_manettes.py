"""Entraînement 1 · Adapter : brancher toutes les manettes 

Le jeu attend des contrôleurs qui respectent le Protocol Controleur :
    prochaine_action() -> str   parmi "haut", "bas", "gauche", "droite", "attaque"

Deux appareils existent déjà, avec leurs propres interfaces (on ne peut pas les modifier) :
- ManetteRetro.lire_code() renvoie un entier : 8 haut, 2 bas, 4 gauche, 6 droite, 5 attaque ;
- ClavierUSB.touche_pressee() renvoie une lettre : "z", "s", "q", "d" ou " " (espace).

Écrivez AdaptateurManette et AdaptateurClavier, puis la fonction
jouer(controleur, n) qui renvoie les n prochaines actions.
Un code ou une touche inconnue donne l'action "rien".
"""


from typing import Protocol


class Controleur(Protocol):
    def prochaine_action(self) -> str: ...


# ---------------------------------------------- appareils existants (non modifiables)
class ManetteRetro:
    def __init__(self, codes):
        self._codes = list(codes)

    def lire_code(self):
        return self._codes.pop(0)


class ClavierUSB:
    def __init__(self, touches):
        self._touches = list(touches)

    def touche_pressee(self):
        return self._touches.pop(0)


# ---------------------------------------------- adaptateurs
# TODO : AdaptateurManette(manette) et AdaptateurClavier(clavier)


def jouer(controleur, n):
    # TODO
    pass


if __name__ == "__main__":
    assert jouer(AdaptateurManette(ManetteRetro([8, 8, 5, 0])), 4) == ["haut", "haut", "attaque", "rien"]
    assert jouer(AdaptateurClavier(ClavierUSB(["q", " ", "x"])), 3) == ["gauche", "attaque", "rien"]
    print("Tous les tests passent !")
