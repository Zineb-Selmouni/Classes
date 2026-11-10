"""Entraînement 5 · Iterator : générateurs et objets itérables (corrigé)

1. compte_a_rebours(n) : un générateur qui produit n, n-1, … 1 puis "Partez !".
2. paliers_xp() : un générateur INFINI des XP cumulées par niveau :
   100, 250, 450, 700… (on ajoute 100, puis 150, puis 200… : +50 à chaque fois).
   Utilisez itertools.islice pour n'en prendre que quelques-uns.
3. Carte(lignes) : itérable ; for x, y, case in carte parcourt toutes les cases
   qui ne sont PAS des murs ("#"), ligne par ligne. Écrivez __iter__ avec yield.
4. Ronde(gardes, tours) : un itérateur « à la main » (__iter__ renvoie self,
   __next__ lève StopIteration) qui fait passer les gardes à tour de rôle,
   pendant `tours` passages au total.
"""
from itertools import islice


def compte_a_rebours(n):
    for i in range(n, 0, -1):
        yield i
    yield "Partez !"


def paliers_xp():
    total, pas = 0, 100
    while True:
        total += pas
        yield total
        pas += 50


class Carte:
    def __init__(self, lignes):
        self.lignes = lignes

    def __iter__(self):
        for y, ligne in enumerate(self.lignes):
            for x, case in enumerate(ligne):
                if case != "#":
                    yield x, y, case


class Ronde:
    def __init__(self, gardes, tours):
        self.gardes = gardes
        self.tours = tours
        self._passage = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._passage >= self.tours:
            raise StopIteration
        garde = self.gardes[self._passage % len(self.gardes)]
        self._passage += 1
        return garde


if __name__ == "__main__":
    assert list(compte_a_rebours(3)) == [3, 2, 1, "Partez !"]
    assert list(islice(paliers_xp(), 5)) == [100, 250, 450, 700, 1000]
    carte = Carte(["#.#", "$.@"])
    assert list(carte) == [(1, 0, "."), (0, 1, "$"), (1, 1, "."), (2, 1, "@")]
    assert [case for _, _, case in carte if case != "."] == ["$", "@"]   # réutilisable
    assert list(Ronde(["Ana", "Bob"], 5)) == ["Ana", "Bob", "Ana", "Bob", "Ana"]
    ronde = Ronde(["Ana"], 1)
    assert next(ronde) == "Ana"
    try:
        next(ronde)
        raise AssertionError("StopIteration attendue")
    except StopIteration:
        pass
    print("Tous les tests passent !")
