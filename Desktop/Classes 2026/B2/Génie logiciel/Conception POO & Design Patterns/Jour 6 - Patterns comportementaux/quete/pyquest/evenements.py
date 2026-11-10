"""Observer : un bus d'événements.

Le combat PUBLIE ce qui se passe ; le journal, les succès (et demain les sons,
les statistiques, l'interface graphique…) S'ABONNENT. Le combat ne les connaît pas.
"""
from collections import defaultdict


class BusEvenements:
    def __init__(self):
        self._abonnes = defaultdict(list)   # nom d'événement -> liste de fonctions

    def abonner(self, evenement, callback):
        # TODO
        pass

    def desabonner(self, evenement, callback):
        # TODO
        pass

    def publier(self, evenement, **donnees):
        # TODO : appeler chaque abonné avec callback(**donnees)
        pass


class Journal:
    """Observateur : garde une trace lisible de tout ce qui se passe.

    Il s'abonne à 5 événements :
      "action"   (message)                 -> la ligne message
      "attaque"  (auteur, cible, degats)   -> "Brakk inflige 7 dégâts à Slime"
      "victoire" (hero, adversaire)        -> "Slime est vaincu !"
      "defaite"  (hero, adversaire)        -> "Brakk est tombé au combat…"
      "succes"   (nom)                     -> "*** Succès débloqué : Premier sang ***"
    """

    def __init__(self, bus):
        self.lignes = []
        # TODO : s'abonner aux 5 événements avec des méthodes sur_action, sur_attaque…


class ChasseurDeSucces:
    """Observateur qui publie à son tour un événement « succes » (nom=...).

    - "Premier sang"   : 1re victoire
    - "Chasseur"       : 3e victoire
    - "Tueur de boss"  : victoire contre un adversaire qui a l'attribut enrage
    - "Coup de maître" : une attaque d'au moins COUP_DE_MAITRE dégâts
    Chaque succès n'est débloqué qu'une fois (liste self.debloques).
    """

    COUP_DE_MAITRE = 20

    def __init__(self, bus):
        self.bus = bus
        self.victoires = 0
        self.debloques = []
        # TODO
