"""Étapes 2 et 3 — fabrique de monstres (registre) et Abstract Factory des biomes."""
from abc import ABC, abstractmethod

from .config import Configuration
from .objets import Parchemin, Potion
from .personnages import Boss, Monstre

# ====================================================================== fabrique simple + registre
_RECETTES = {}


def enregistrer(type_monstre):
    """Décorateur : @enregistrer("slime") au-dessus d'une fonction recette(niveau) -> Monstre."""
    # TODO


# TODO : recettes « slime » (PV 15 + 5 × niveau, dégâts 2 + niveau, XP 10 × niveau),
#        « gobelin » (25 + 8n, 4 + n, 20n) et « roi gobelin » (un Boss : 60 + 20n, 6 + 2n, 80n)


def types_connus():
    return sorted(_RECETTES)


def creer_monstre(type_monstre, niveau=1):
    """ValueError si inconnu. Multiplie PV et dégâts par Configuration().multiplicateur
    (arrondis, au moins 1 dégât)."""
    # TODO


# ====================================================================== Abstract Factory
# TODO : FabriqueDeBiome (abstraite : creer_monstre(niveau), creer_tresor(), decrire_lieu())
#        FabriqueForet  : Monstre("Loup sauvage", 20 + 6n, 4 + n, 15n), Potion("Sève de chêne", 30)
#        FabriqueVolcan : Monstre("Salamandre", 30 + 8n, 6 + 2n, 25n), Parchemin("Parchemin de lave", 30)


def generer_rencontre(fabrique, niveau=1):
    """Renvoie {"lieu": ..., "monstre": ..., "tresor": ...} sans connaître le biome."""
    # TODO
