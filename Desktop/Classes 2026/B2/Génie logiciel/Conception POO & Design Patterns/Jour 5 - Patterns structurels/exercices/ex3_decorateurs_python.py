"""Entraînement 3 · Les décorateurs de Python (@) 

Le mot « décorateur » désigne aussi la syntaxe @ de Python : une fonction qui
enveloppe une autre fonction. Même idée que le pattern, appliquée aux fonctions.
1. @compter_appels : ajoute à la fonction un attribut appels (nombre d'appels).
2. @journaliser(journal) : ajoute "nom_fonction(args) -> résultat" à la liste journal.
3. @memoiser : garde en cache les résultats déjà calculés (arguments hachables).
Utilisez functools.wraps pour conserver le nom de la fonction décorée.
"""


import functools


def compter_appels(fonction):
    # TODO
    pass


def journaliser(journal):
    # TODO : un décorateur AVEC paramètre (trois niveaux de fonctions)
    pass


def memoiser(fonction):
    # TODO
    pass


JOURNAL = []


@journaliser(JOURNAL)
def degats(base, multiplicateur):
    return base * multiplicateur


@compter_appels
@memoiser
def xp_requise(niveau):
    """XP totale pour atteindre un niveau (récursif, donc coûteux sans cache)."""
    return 0 if niveau <= 1 else xp_requise(niveau - 1) + 100 * (niveau - 1)


if __name__ == "__main__":
    assert degats(10, 2) == 20 and JOURNAL == ["degats(10, 2) -> 20"]
    assert xp_requise(5) == 1000
    appels = xp_requise.appels
    xp_requise(5)
    assert xp_requise.appels == appels + 1          # compté…
    assert xp_requise.__name__ == "xp_requise"       # functools.wraps
    assert xp_requise.__doc__.startswith("XP totale")
    print("Tous les tests passent !")
