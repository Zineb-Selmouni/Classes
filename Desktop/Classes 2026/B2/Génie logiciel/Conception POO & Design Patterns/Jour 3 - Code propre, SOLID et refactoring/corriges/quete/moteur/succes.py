"""Les succès : une liste de règles. Ajouter un succès = ajouter une ligne. (O de SOLID.)"""
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Succes:
    nom: str
    condition: Callable[[object], bool]


REGLES = [
    Succes("Premier sang", lambda h: h.monstres_tues >= 1),
    Succes("Chasseur", lambda h: h.monstres_tues >= 5),
    Succes("Riche", lambda h: h.or_ >= 100),
    Succes("Vétéran", lambda h: h.niveau >= 3),
]


class VerificateurDeSucces:
    def __init__(self, affichage, regles=REGLES):
        self.affichage = affichage
        self.regles = regles

    def verifier(self, hero):
        for regle in self.regles:
            if regle.nom not in hero.succes and regle.condition(hero):
                hero.succes.append(regle.nom)
                self.affichage.afficher(f"Succès débloqué : {regle.nom}")
