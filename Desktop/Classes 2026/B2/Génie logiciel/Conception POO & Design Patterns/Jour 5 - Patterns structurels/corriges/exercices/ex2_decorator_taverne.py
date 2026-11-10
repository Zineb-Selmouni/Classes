"""Entraînement 2 · Decorator : les boissons de la taverne (corrigé)

La taverne sert des boissons de base, et des suppléments qu'on peut cumuler.
Créer une classe par combinaison (ThéAuLaitAvecMiel…) serait une explosion.
1. Une classe abstraite Boisson avec description() -> str et prix() -> float.
2. Les boissons de base : The (2.0) et Hydromel (4.5).
3. Un décorateur abstrait Supplement qui enveloppe une Boisson, et trois suppléments :
   Lait (+0.5, « au lait »), Miel (+0.8, « au miel »), Epices (+1.0, « aux épices »).
4. On peut empiler : Miel(Lait(The())) -> « Thé au lait au miel », 3.3.
"""
from abc import ABC, abstractmethod


class Boisson(ABC):
    @abstractmethod
    def description(self) -> str: ...

    @abstractmethod
    def prix(self) -> float: ...


class The(Boisson):
    def description(self):
        return "Thé"

    def prix(self):
        return 2.0


class Hydromel(Boisson):
    def description(self):
        return "Hydromel"

    def prix(self):
        return 4.5


class Supplement(Boisson):
    nom = "supplément"
    cout = 0.0

    def __init__(self, boisson: Boisson):
        self._boisson = boisson

    def description(self):
        return f"{self._boisson.description()} {self.nom}"

    def prix(self):
        return round(self._boisson.prix() + self.cout, 2)


class Lait(Supplement):
    nom, cout = "au lait", 0.5


class Miel(Supplement):
    nom, cout = "au miel", 0.8


class Epices(Supplement):
    nom, cout = "aux épices", 1.0


if __name__ == "__main__":
    b = Miel(Lait(The()))
    assert b.description() == "Thé au lait au miel" and b.prix() == 3.3
    h = Epices(Epices(Hydromel()))
    assert h.description() == "Hydromel aux épices aux épices" and h.prix() == 6.5
    assert isinstance(b, Boisson)
    print("Tous les tests passent !")
