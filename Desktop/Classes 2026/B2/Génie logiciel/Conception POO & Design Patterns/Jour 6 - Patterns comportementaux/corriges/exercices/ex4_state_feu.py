"""Entraînement 4 · State : le feu tricolore de la capitale (corrigé)

Version « avant », pleine de if :
    if self.couleur == "vert": self.couleur = "orange"
    elif self.couleur == "orange": self.couleur = "rouge"
    elif ...                      # et la même cascade dans peut_passer, panne…
Réécrivez-la avec le pattern State :
1. Une classe abstraite EtatFeu avec couleur, suivant(feu) et peut_passer().
2. Vert -> Orange -> Rouge -> Vert. On ne peut passer qu'au vert.
3. Clignotant (panne) : couleur "orange clignotant", on peut passer (prudemment),
   suivant() ne change rien.
4. Feu : suivant(), peut_passer(), panne() -> Clignotant, reparer() -> Rouge,
   et la propriété couleur. Le Feu ne contient AUCUN if sur son état.
"""
from abc import ABC, abstractmethod


class EtatFeu(ABC):
    couleur = "?"

    @abstractmethod
    def suivant(self, feu): ...

    @abstractmethod
    def peut_passer(self) -> bool: ...


class Vert(EtatFeu):
    couleur = "vert"

    def suivant(self, feu):
        feu.etat = Orange()

    def peut_passer(self):
        return True


class Orange(EtatFeu):
    couleur = "orange"

    def suivant(self, feu):
        feu.etat = Rouge()

    def peut_passer(self):
        return False


class Rouge(EtatFeu):
    couleur = "rouge"

    def suivant(self, feu):
        feu.etat = Vert()

    def peut_passer(self):
        return False


class Clignotant(EtatFeu):
    couleur = "orange clignotant"

    def suivant(self, feu):
        pass                       # en panne : le cycle est suspendu

    def peut_passer(self):
        return True


class Feu:
    def __init__(self):
        self.etat = Rouge()

    @property
    def couleur(self):
        return self.etat.couleur

    def suivant(self):
        self.etat.suivant(self)

    def peut_passer(self):
        return self.etat.peut_passer()

    def panne(self):
        self.etat = Clignotant()

    def reparer(self):
        self.etat = Rouge()


if __name__ == "__main__":
    feu = Feu()
    couleurs = []
    for _ in range(4):
        couleurs.append(feu.couleur)
        feu.suivant()
    assert couleurs == ["rouge", "vert", "orange", "rouge"]
    assert feu.couleur == "vert" and feu.peut_passer()
    feu.panne()
    feu.suivant()
    assert feu.couleur == "orange clignotant" and feu.peut_passer()
    feu.reparer()
    assert feu.couleur == "rouge" and not feu.peut_passer()
    print("Tous les tests passent !")
