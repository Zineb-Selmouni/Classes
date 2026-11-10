"""Entraînement 5 · D comme Dependency Inversion : le corbeau messager 

Version « avant » :

    class Messagerie:
        def __init__(self):
            self.corbeau = CorbeauRoyal()      # dépendance codée en dur

        def prevenir_guilde(self, message):
            self.corbeau.envoyer("guilde@pyquest", message)

Impossible de tester sans vraiment envoyer un corbeau, et impossible de
passer aux pigeons voyageurs sans modifier Messagerie.

1. Définissez un Protocol Messager (méthode envoyer(destinataire, message) -> bool).
2. Messagerie reçoit son messager dans __init__ (injection de dépendance).
3. Écrivez un FauxMessager pour les tests, qui mémorise les envois.
4. prevenir_guilde renvoie True si l'envoi a réussi ; si le messager échoue,
   Messagerie réessaie une fois (2 tentatives au maximum).
"""


from typing import Protocol


class CorbeauRoyal:
    def envoyer(self, destinataire, message):
        print(f"Croâ ! Le corbeau vole vers {destinataire} : {message}")
        return True


class Messagerie:
    def __init__(self):
        self.corbeau = CorbeauRoyal()      # TODO : injecter le messager à la place

    def prevenir_guilde(self, message):
        # TODO : renvoyer True/False, 2 tentatives au maximum
        self.corbeau.envoyer("guilde@pyquest", message)


# TODO : le Protocol Messager et la classe FauxMessager(echecs=0) qui mémorise les envois


if __name__ == "__main__":
    faux = FauxMessager()
    assert Messagerie(faux).prevenir_guilde("Dragon en vue !") is True
    assert faux.envois == [("guilde@pyquest", "Dragon en vue !")]
    capricieux = FauxMessager(echecs=1)
    assert Messagerie(capricieux).prevenir_guilde("Retour au camp") is True
    assert len(capricieux.envois) == 2
    assert Messagerie(FauxMessager(echecs=5)).prevenir_guilde("Perdu") is False
    print("Tous les tests passent !")
