"""Moteur de PyQuest.

Au début de la quête 3, ce fichier exporte l'ancienne Partie (legacy.py).
À la fin, il exporte la nouvelle : les tests du golden master doivent
passer avec les deux.
"""
from .partie import Partie  # avant : from .legacy import Partie
