"""Entraînement 1 · Adapter : brancher toutes les manettes (corrigé)

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
class AdaptateurManette:
    CODES = {8: "haut", 2: "bas", 4: "gauche", 6: "droite", 5: "attaque"}

    def __init__(self, manette: ManetteRetro):
        self._manette = manette

    def prochaine_action(self):
        return self.CODES.get(self._manette.lire_code(), "rien")


class AdaptateurClavier:
    TOUCHES = {"z": "haut", "s": "bas", "q": "gauche", "d": "droite", " ": "attaque"}

    def __init__(self, clavier: ClavierUSB):
        self._clavier = clavier

    def prochaine_action(self):
        return self.TOUCHES.get(self._clavier.touche_pressee(), "rien")


def jouer(controleur: Controleur, n):
    return [controleur.prochaine_action() for _ in range(n)]


if __name__ == "__main__":
    assert jouer(AdaptateurManette(ManetteRetro([8, 8, 5, 0])), 4) == ["haut", "haut", "attaque", "rien"]
    assert jouer(AdaptateurClavier(ClavierUSB(["q", " ", "x"])), 3) == ["gauche", "attaque", "rien"]
    print("Tous les tests passent !")
