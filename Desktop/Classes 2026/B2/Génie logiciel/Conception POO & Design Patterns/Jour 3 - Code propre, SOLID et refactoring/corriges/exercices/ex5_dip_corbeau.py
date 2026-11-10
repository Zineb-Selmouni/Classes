"""Entraînement 5 · D comme Dependency Inversion : le corbeau messager (corrigé)

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


class Messager(Protocol):
    def envoyer(self, destinataire: str, message: str) -> bool: ...


class CorbeauRoyal:
    def envoyer(self, destinataire, message):
        print(f"Croâ ! Le corbeau vole vers {destinataire} : {message}")
        return True


class Messagerie:
    def __init__(self, messager: Messager):
        self.messager = messager

    def prevenir_guilde(self, message):
        for _ in range(2):
            if self.messager.envoyer("guilde@pyquest", message):
                return True
        return False


class FauxMessager:
    def __init__(self, echecs=0):
        self.envois = []
        self.echecs_restants = echecs

    def envoyer(self, destinataire, message):
        self.envois.append((destinataire, message))
        if self.echecs_restants > 0:
            self.echecs_restants -= 1
            return False
        return True


if __name__ == "__main__":
    faux = FauxMessager()
    assert Messagerie(faux).prevenir_guilde("Dragon en vue !") is True
    assert faux.envois == [("guilde@pyquest", "Dragon en vue !")]
    capricieux = FauxMessager(echecs=1)
    assert Messagerie(capricieux).prevenir_guilde("Retour au camp") is True
    assert len(capricieux.envois) == 2
    assert Messagerie(FauxMessager(echecs=5)).prevenir_guilde("Perdu") is False
    print("Tous les tests passent !")
