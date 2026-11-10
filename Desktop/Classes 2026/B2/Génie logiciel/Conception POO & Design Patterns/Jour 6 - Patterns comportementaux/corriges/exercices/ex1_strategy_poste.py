"""Entraînement 1 · Strategy : la poste du royaume (corrigé)

La poste propose plusieurs façons de livrer un colis. Chaque mode de livraison
calcule ses frais différemment : c'est une stratégie interchangeable.
  Pigeon : 2 + 0.5 par kg (refuse les colis de plus de 1 kg : ValueError)
  Cheval : 5 + 0.1 par km
  Dragon : 50, quel que soit le colis
1. Écrivez les trois stratégies (une méthode frais(colis)).
2. Poste(strategie) : envoyer(colis) -> "Lettre : 2.10 pièces" ;
   on peut changer de stratégie avec changer_mode(strategie).
3. le_moins_cher(colis, modes) renvoie le nom (classe) du mode le moins cher
   parmi ceux qui acceptent le colis.
4. Une simple fonction peut aussi servir de stratégie : vérifiez-le avec
   Poste(lambda colis: 1).  (Attention : la poste appelle alors strategie(colis).)
"""
from dataclasses import dataclass


@dataclass
class Colis:
    nom: str
    poids: float      # kg
    distance: float   # km


class Pigeon:
    def frais(self, colis):
        if colis.poids > 1:
            raise ValueError("Un pigeon ne porte pas plus de 1 kg")
        return 2 + 0.5 * colis.poids


class Cheval:
    def frais(self, colis):
        return 5 + 0.1 * colis.distance


class Dragon:
    def frais(self, colis):
        return 50


class Poste:
    def __init__(self, strategie):
        self.strategie = strategie

    def changer_mode(self, strategie):
        self.strategie = strategie

    def _frais(self, colis):
        # une stratégie peut être un objet (avec frais) ou une simple fonction
        if callable(self.strategie):
            return self.strategie(colis)
        return self.strategie.frais(colis)

    def envoyer(self, colis):
        return f"{colis.nom} : {self._frais(colis):.2f} pièces"


def le_moins_cher(colis, modes):
    possibles = {}
    for mode in modes:
        try:
            possibles[type(mode).__name__] = mode.frais(colis)
        except ValueError:
            pass
    return min(possibles, key=possibles.get)


if __name__ == "__main__":
    lettre = Colis("Lettre", 0.2, 30)
    armure = Colis("Armure", 25, 400)
    poste = Poste(Pigeon())
    assert poste.envoyer(lettre) == "Lettre : 2.10 pièces"
    poste.changer_mode(Cheval())
    assert poste.envoyer(lettre) == "Lettre : 8.00 pièces"
    assert poste.envoyer(armure) == "Armure : 45.00 pièces"
    poste.changer_mode(Dragon())
    assert poste.envoyer(armure) == "Armure : 50.00 pièces"
    modes = [Pigeon(), Cheval(), Dragon()]
    assert le_moins_cher(lettre, modes) == "Pigeon"
    assert le_moins_cher(armure, modes) == "Cheval"
    assert le_moins_cher(Colis("Coffre", 40, 800), modes) == "Dragon"
    assert Poste(lambda colis: 1).envoyer(lettre) == "Lettre : 1.00 pièces"
    print("Tous les tests passent !")
