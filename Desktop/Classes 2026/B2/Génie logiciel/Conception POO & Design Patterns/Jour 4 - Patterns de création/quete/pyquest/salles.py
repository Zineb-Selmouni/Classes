"""Étape 4 — Factory Method : chaque type de salle décide quel monstre elle crée."""
from abc import ABC, abstractmethod

from .fabriques import creer_monstre


class Salle(ABC):
    def __init__(self, niveau=1):
        self.niveau = niveau

    # TODO : méthode fabrique abstraite creer_monstre()

    def entrer(self, hero):
        """Renvoie (texte, monstre). Texte : "Brakk entre dans <nom> : un <monstre> surgit !" """
        # TODO


# TODO : SalleOrdinaire (nom = "une salle humide" ; slime avant le niveau 3, gobelin ensuite)
#        SalleDuTrone (nom = "la salle du trône" ; roi gobelin)
