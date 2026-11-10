"""Entraînement 3 · La durée des sorts (corrigé)

Créez une classe Duree(minutes=0, secondes=0) :
- elle se normalise : Duree(1, 75) vaut 2 min 15 s ;
- Duree.depuis_secondes(135) est un constructeur alternatif (classmethod) ;
- __str__ -> "2 min 15 s" ; __repr__ -> "Duree(2, 15)" ;
- d1 + d2 renvoie une nouvelle Duree ;
- d1 == d2 et d1 < d2 fonctionnent (donc sorted() aussi).
"""
from functools import total_ordering


@total_ordering
class Duree:
    def __init__(self, minutes=0, secondes=0):
        total = minutes * 60 + secondes
        if total < 0:
            raise ValueError("Une durée ne peut pas être négative")
        self.minutes, self.secondes = divmod(total, 60)

    @classmethod
    def depuis_secondes(cls, secondes):
        return cls(0, secondes)

    @property
    def total_secondes(self):
        return self.minutes * 60 + self.secondes

    def __str__(self):
        return f"{self.minutes} min {self.secondes:02d} s"

    def __repr__(self):
        return f"Duree({self.minutes}, {self.secondes})"

    def __add__(self, autre):
        if not isinstance(autre, Duree):
            return NotImplemented
        return Duree.depuis_secondes(self.total_secondes + autre.total_secondes)

    def __eq__(self, autre):
        if not isinstance(autre, Duree):
            return NotImplemented
        return self.total_secondes == autre.total_secondes

    def __lt__(self, autre):
        if not isinstance(autre, Duree):
            return NotImplemented
        return self.total_secondes < autre.total_secondes

    def __hash__(self):
        return hash(self.total_secondes)


if __name__ == "__main__":
    d = Duree(1, 75)
    assert (d.minutes, d.secondes) == (2, 15)
    assert str(d) == "2 min 15 s" and repr(d) == "Duree(2, 15)"
    assert Duree.depuis_secondes(135) == d
    assert Duree(0, 50) + Duree(0, 20) == Duree(1, 10)
    assert Duree(0, 30) < Duree(1, 0) and Duree(2, 0) >= Duree(1, 59)
    sorts = [Duree(3), Duree(0, 45), Duree(1, 30)]
    assert sorted(sorts) == [Duree(0, 45), Duree(1, 30), Duree(3)]
    print("Tous les tests passent !")
