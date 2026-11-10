"""State : l'état d'un personnage change son comportement au début de chaque tour.

Plutôt qu'un attribut texte (« empoisonné ») et des if partout, chaque état est
un objet qui sait ce qu'il fait, et qui décide lui-même de l'état suivant.
"""
from abc import ABC, abstractmethod


class Etat(ABC):
    nom = "?"

    @abstractmethod
    def debut_de_tour(self, perso):
        """Renvoie (peut_agir, message ou None). Peut changer perso.etat."""

    def __str__(self):
        return self.nom


class Normal(Etat):
    nom = "normal"

    def debut_de_tour(self, perso):
        return True, None


class Empoisonne(Etat):
    nom = "empoisonné"

    def __init__(self, tours=3, degats=3):
        self.tours = tours
        self.degats = degats

    def debut_de_tour(self, perso):
        perso.recevoir_degats(self.degats)
        self.tours -= 1
        if self.tours == 0:
            perso.etat = Normal()                 # l'état décide de la transition
        return True, f"{perso.nom} souffre du poison : -{self.degats} PV"


class Etourdi(Etat):
    nom = "étourdi"

    def debut_de_tour(self, perso):
        perso.etat = Normal()
        return False, f"{perso.nom} est étourdi et passe son tour"
