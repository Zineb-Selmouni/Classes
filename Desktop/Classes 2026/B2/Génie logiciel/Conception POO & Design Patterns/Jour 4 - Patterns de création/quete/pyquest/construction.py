"""Étape 5 — Builder : construire un héros pas à pas."""
from .objets import Arme
from .personnages import Archer, Guerrier, Mage

CLASSES = {"guerrier": Guerrier, "mage": Mage, "archer": Archer}


class HeroBuilder:
    """nomme(nom), de_classe(classe), arme(arme), avec(objet), au_niveau(n), construire().
    Chaque méthode renvoie self. construire() vérifie le nom et la classe (ValueError)."""

    # TODO


def hero_de_depart(nom, classe):
    """Le directeur : arme de départ selon la classe + une Petite potion (20)."""
    # TODO
