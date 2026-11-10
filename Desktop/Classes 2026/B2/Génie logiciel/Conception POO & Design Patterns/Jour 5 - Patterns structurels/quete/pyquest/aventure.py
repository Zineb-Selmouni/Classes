"""Étape 5 — Facade : une porte d'entrée simple vers tout le moteur du jeu.

Aventure(tableau=None, rng=None)
- nouvelle_partie(nom, classe, difficulte="normal") : règle la Configuration, crée le héros
  avec hero_de_depart, remet le score à 0, renvoie str(hero) ;
- explorer(biome) : "forêt" ou "volcan" (ValueError sinon ; RuntimeError sans partie) ;
  génère une rencontre, lance le combat, ajoute le trésor et l'XP du monstre au score
  en cas de victoire, renvoie le journal (le lieu en 1re ligne, "Trésor : …" en dernière) ;
- terminer() : enregistre le score dans le tableau, renvoie les meilleurs scores.
"""
import random

from .combat import combat
from .config import Configuration
from .construction import hero_de_depart
from .fabriques import FabriqueForet, FabriqueVolcan, generer_rencontre
from .scores import TableauEnMemoire

BIOMES = {"forêt": FabriqueForet, "volcan": FabriqueVolcan}

# TODO
