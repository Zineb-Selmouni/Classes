"""Entraînement 4 · L et I : des créatures qui ne savent pas tout faire 

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


# TODO : les Protocol Volant, Nageur, Lanceur (@runtime_checkable)


class Gobelin:
    nom = "Gobelin"


# TODO : Griffon (vole), Dragon (vole, nage, lance des sorts), Sirene (nage, lance des sorts)
# Phrases attendues : voir les tests en bas du fichier


def survol(creatures):
    # TODO : ne faire voler que les Volant
    pass


def capacites(creature):
    # TODO : ["vol", "nage", "magie"] selon les protocoles respectés
    pass


if __name__ == "__main__":
    bestiaire = [Gobelin(), Griffon(), Dragon(), Sirene()]
    assert survol(bestiaire) == ["Le griffon plane au-dessus du donjon", "Le dragon s'envole"]
    assert capacites(Dragon()) == ["vol", "nage", "magie"]
    assert capacites(Gobelin()) == []
    assert capacites(Sirene()) == ["nage", "magie"]
    assert not hasattr(Gobelin(), "voler")  # plus de méthode qui « fait semblant »
    print("Tous les tests passent !")
