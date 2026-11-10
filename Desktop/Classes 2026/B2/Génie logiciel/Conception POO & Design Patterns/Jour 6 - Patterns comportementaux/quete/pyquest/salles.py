"""Factory Method : chaque type de salle décide quel monstre elle fait apparaître."""
from abc import ABC, abstractmethod

from .fabriques import creer_monstre


class Salle(ABC):
    def __init__(self, niveau=1):
        self.niveau = niveau

    @abstractmethod
    def creer_monstre(self):
        """La méthode fabrique : redéfinie par chaque sous-classe."""

    def entrer(self, hero):
        """Le même déroulé pour toutes les salles ; seul le monstre change."""
        monstre = self.creer_monstre()
        return f"{hero.nom} entre dans {self.nom} : un {monstre.nom} surgit !", monstre


class SalleOrdinaire(Salle):
    nom = "une salle humide"

    def creer_monstre(self):
        return creer_monstre("slime" if self.niveau < 3 else "gobelin", self.niveau)


class SalleDuTrone(Salle):
    nom = "la salle du trône"

    def creer_monstre(self):
        return creer_monstre("roi gobelin", self.niveau)
