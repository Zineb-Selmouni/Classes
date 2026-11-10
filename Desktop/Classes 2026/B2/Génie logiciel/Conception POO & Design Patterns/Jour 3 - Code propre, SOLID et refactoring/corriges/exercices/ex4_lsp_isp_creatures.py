"""Entraînement 4 · L et I : des créatures qui ne savent pas tout faire (corrigé)

Version « avant » : une seule classe mère impose voler(), nager() et
lancer_sort() à toutes les créatures :

    class Creature:
        def voler(self): ...
        def nager(self): ...
        def lancer_sort(self): ...

    class Gobelin(Creature):
        def voler(self):
            raise NotImplementedError("un gobelin ne vole pas")   # LSP violé !
        ...

Corrigez avec de petites interfaces (I) : les Protocol Volant, Nageur et
Lanceur. Chaque créature n'implémente que ce qu'elle sait vraiment faire,
et la fonction survol(creatures) ne reçoit plus que des Volant (L respecté).
"""
from typing import Protocol, runtime_checkable


@runtime_checkable
class Volant(Protocol):
    def voler(self) -> str: ...


@runtime_checkable
class Nageur(Protocol):
    def nager(self) -> str: ...


@runtime_checkable
class Lanceur(Protocol):
    def lancer_sort(self) -> str: ...


class Gobelin:
    nom = "Gobelin"
    # ne vole pas, ne nage pas, ne lance pas de sort : et c'est très bien


class Griffon:
    nom = "Griffon"

    def voler(self):
        return "Le griffon plane au-dessus du donjon"


class Dragon:
    nom = "Dragon"

    def voler(self):
        return "Le dragon s'envole"

    def nager(self):
        return "Le dragon plonge dans le lac"

    def lancer_sort(self):
        return "Le dragon crache un sort de feu"


class Sirene:
    nom = "Sirène"

    def nager(self):
        return "La sirène nage"

    def lancer_sort(self):
        return "La sirène chante un sort"


def survol(creatures):
    return [c.voler() for c in creatures if isinstance(c, Volant)]


def capacites(creature):
    return [nom for nom, proto in (("vol", Volant), ("nage", Nageur), ("magie", Lanceur)) if isinstance(creature, proto)]


if __name__ == "__main__":
    bestiaire = [Gobelin(), Griffon(), Dragon(), Sirene()]
    assert survol(bestiaire) == ["Le griffon plane au-dessus du donjon", "Le dragon s'envole"]
    assert capacites(Dragon()) == ["vol", "nage", "magie"]
    assert capacites(Gobelin()) == []
    assert capacites(Sirene()) == ["nage", "magie"]
    assert not hasattr(Gobelin(), "voler")  # plus de méthode qui « fait semblant »
    print("Tous les tests passent !")
