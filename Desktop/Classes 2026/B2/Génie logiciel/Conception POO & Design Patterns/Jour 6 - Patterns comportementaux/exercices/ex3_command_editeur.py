"""Entraînement 3 · Command : l'éditeur de parchemins 

Un mini éditeur de texte, avec annuler (Ctrl+Z) et refaire (Ctrl+Y).
1. Editeur : un attribut texte (chaîne vide au départ). C'est le « récepteur ».
2. Trois commandes, avec executer() et annuler() :
   Ecrire(editeur, texte)    ajoute texte à la fin
   Effacer(editeur, n)       efface les n derniers caractères
   Majuscules(editeur)       met tout le texte en majuscules
   Chaque commande mémorise ce dont elle a besoin pour s'annuler.
3. Historique : executer(commande), annuler(), refaire().
   Une nouvelle commande vide la pile « refaire ».
"""


from abc import ABC, abstractmethod


class Editeur:
    def __init__(self):
        self.texte = ""


class Commande(ABC):
    def __init__(self, editeur):
        self.editeur = editeur

    @abstractmethod
    def executer(self): ...

    @abstractmethod
    def annuler(self): ...


# TODO : Ecrire(editeur, texte), Effacer(editeur, n), Majuscules(editeur)


class Historique:
    # TODO : executer, annuler, refaire
    pass


if __name__ == "__main__":
    e, h = Editeur(), Historique()
    h.executer(Ecrire(e, "Bonjour"))
    h.executer(Ecrire(e, " monde"))
    h.executer(Effacer(e, 6))
    assert e.texte == "Bonjour"
    h.annuler()
    assert e.texte == "Bonjour monde"
    h.refaire()
    assert e.texte == "Bonjour"
    h.executer(Majuscules(e))
    assert e.texte == "BONJOUR"
    h.annuler()
    h.annuler()
    assert e.texte == "Bonjour monde"
    h.executer(Ecrire(e, " !"))
    h.refaire()                              # rien à refaire : nouvelle commande
    assert e.texte == "Bonjour monde !"
    for _ in range(10):
        h.annuler()                          # annuler sur une pile vide : sans effet
    assert e.texte == ""
    print("Tous les tests passent !")
