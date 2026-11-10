"""Entraînement 3 · Command : l'éditeur de parchemins (corrigé)

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


class Ecrire(Commande):
    def __init__(self, editeur, texte):
        super().__init__(editeur)
        self.texte = texte

    def executer(self):
        self.editeur.texte += self.texte

    def annuler(self):
        self.editeur.texte = self.editeur.texte[: -len(self.texte)]


class Effacer(Commande):
    def __init__(self, editeur, n):
        super().__init__(editeur)
        self.n = n
        self._efface = ""

    def executer(self):
        self._efface = self.editeur.texte[-self.n:]
        self.editeur.texte = self.editeur.texte[: -self.n]

    def annuler(self):
        self.editeur.texte += self._efface


class Majuscules(Commande):
    def executer(self):
        self._avant = self.editeur.texte
        self.editeur.texte = self.editeur.texte.upper()

    def annuler(self):
        self.editeur.texte = self._avant


class Historique:
    def __init__(self):
        self._faites, self._annulees = [], []

    def executer(self, commande):
        commande.executer()
        self._faites.append(commande)
        self._annulees.clear()

    def annuler(self):
        if self._faites:
            commande = self._faites.pop()
            commande.annuler()
            self._annulees.append(commande)

    def refaire(self):
        if self._annulees:
            commande = self._annulees.pop()
            commande.executer()
            self._faites.append(commande)


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
