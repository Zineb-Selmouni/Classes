"""Où vont les messages du jeu ? (D de SOLID : on dépend d'une abstraction.)"""
from typing import Protocol


class Affichage(Protocol):
    def afficher(self, message: str) -> None: ...


class AffichageConsole:
    def afficher(self, message):
        print(message)


class AffichageMemoire:
    """Pour les tests : garde les messages dans une liste au lieu de les imprimer."""

    def __init__(self):
        self.messages = []

    def afficher(self, message):
        self.messages.append(message)
