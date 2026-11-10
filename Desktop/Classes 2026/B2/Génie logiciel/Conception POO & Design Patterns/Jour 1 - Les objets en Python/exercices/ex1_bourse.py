"""Entraînement 1 · La bourse du héros 

Créez une classe Bourse qui contient des pièces d'or :
- Bourse(or_initial=0) ; refuser un montant initial négatif (ValueError) ;
- ajouter(montant) : montant strictement positif, sinon ValueError ;
- depenser(montant) : renvoie True et retire l'or si c'est possible,
  renvoie False sans rien changer si la bourse ne contient pas assez ;
- l'attribut or_ est lisible ;
- un attribut de classe total_en_jeu compte l'or ajouté dans TOUTES les bourses.
"""


class Bourse:
    total_en_jeu = 0  # attribut de classe

    def __init__(self, or_initial=0):
        # TODO : refuser un montant négatif, initialiser self.or_, mettre à jour total_en_jeu
        pass

    def ajouter(self, montant):
        # TODO
        pass

    def depenser(self, montant):
        # TODO : renvoyer True / False
        pass


if __name__ == "__main__":
    b = Bourse(50)
    b.ajouter(30)
    assert b.or_ == 80
    assert b.depenser(100) is False and b.or_ == 80
    assert b.depenser(20) is True and b.or_ == 60
    autre = Bourse(10)
    assert Bourse.total_en_jeu == 70
    for mauvais in (lambda: Bourse(-5), lambda: b.ajouter(0), lambda: b.depenser(-1)):
        try:
            mauvais()
        except ValueError:
            pass
        else:
            raise AssertionError("ValueError attendue")
    print("Tous les tests passent !")
