"""Entraînement 5 · Prototype et Singleton 

Partie A — Prototype
  Une Escouade a un nom et une liste de soldats (des dictionnaires).
  1. cloner_surface() renvoie une copie superficielle (copy.copy) ;
  2. cloner() renvoie une copie profonde (copy.deepcopy) ;
  Les tests montrent la différence : modifier un soldat du clone superficiel
  modifie aussi l'original !

Partie B — Singleton
  3. JournalDeJeu est un Singleton (via __new__) avec une liste d'entrées et
     une méthode ecrire(message). Deux « créations » renvoient le même objet.
"""


import copy


class Escouade:
    def __init__(self, nom, soldats):
        self.nom = nom
        self.soldats = soldats

    # TODO : cloner_surface() et cloner()


class JournalDeJeu:
    # TODO : un Singleton avec __new__, une liste entrees et une méthode ecrire(message)
    pass


if __name__ == "__main__":
    modele = Escouade("Gardes", [{"nom": "Garde 1", "pv": 30}, {"nom": "Garde 2", "pv": 30}])

    surface = modele.cloner_surface()
    surface.soldats[0]["pv"] = 0
    assert modele.soldats[0]["pv"] == 0          # piège : la liste est partagée !

    modele.soldats[0]["pv"] = 30
    profonde = modele.cloner()
    profonde.soldats[0]["pv"] = 0
    profonde.nom = "Gardes d'élite"
    assert modele.soldats[0]["pv"] == 30 and modele.nom == "Gardes"

    JournalDeJeu().ecrire("Début de la partie")
    JournalDeJeu().ecrire("Un gobelin apparaît")
    assert JournalDeJeu() is JournalDeJeu()
    assert JournalDeJeu().entrees == ["Début de la partie", "Un gobelin apparaît"]
    print("Tous les tests passent !")
