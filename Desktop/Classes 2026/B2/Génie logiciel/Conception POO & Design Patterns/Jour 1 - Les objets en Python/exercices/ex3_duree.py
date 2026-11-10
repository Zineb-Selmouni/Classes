"""Entraînement 3 · La durée des sorts 

Créez une classe Duree(minutes=0, secondes=0) :
- elle se normalise : Duree(1, 75) vaut 2 min 15 s ;
- Duree.depuis_secondes(135) est un constructeur alternatif (classmethod) ;
- __str__ -> "2 min 15 s" ; __repr__ -> "Duree(2, 15)" ;
- d1 + d2 renvoie une nouvelle Duree ;
- d1 == d2 et d1 < d2 fonctionnent (donc sorted() aussi).
"""


class Duree:
    def __init__(self, minutes=0, secondes=0):
        # TODO : normaliser (75 secondes = 1 min 15 s) ; refuser une durée négative
        pass

    # TODO : @classmethod depuis_secondes(cls, secondes)

    # TODO : __str__, __repr__, __add__, __eq__, __lt__ (et les autres comparaisons !)
    # Indice : regardez functools.total_ordering


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
