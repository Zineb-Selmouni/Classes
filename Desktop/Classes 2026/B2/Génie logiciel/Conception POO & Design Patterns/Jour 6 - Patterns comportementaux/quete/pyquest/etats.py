"""State : l'état d'un personnage change son comportement au début de chaque tour.

Plutôt qu'un attribut texte (« empoisonné ») et des if partout, chaque état est
un objet qui sait ce qu'il fait, et qui décide lui-même de l'état suivant.

N'oubliez pas : dans personnages.py, tout Personnage commence avec self.etat = Normal().
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


# TODO : Empoisonne(tours=3, degats=3)
#   inflige ses dégâts, décrémente tours, repasse à Normal() quand tours == 0
#   message : "Brakk souffre du poison : -3 PV" ; le personnage peut agir


# TODO : Etourdi()
#   le personnage ne peut pas agir ce tour-ci, puis repasse à Normal()
#   message : "Brakk est étourdi et passe son tour"
