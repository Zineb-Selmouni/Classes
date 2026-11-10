"""Où sont rangées les sauvegardes ? Peu importe pour la Partie. (D de SOLID.)"""
import json
from typing import Protocol


class Stockage(Protocol):
    def ecrire(self, donnees: dict) -> None: ...
    def lire(self) -> dict: ...


class StockageFichier:
    def __init__(self, chemin="sauvegarde.json"):
        self.chemin = chemin

    def ecrire(self, donnees):
        with open(self.chemin, "w", encoding="utf-8") as f:
            json.dump(donnees, f)

    def lire(self):
        with open(self.chemin, encoding="utf-8") as f:
            return json.load(f)


class StockageMemoire:
    """Pour les tests (et pour une future sauvegarde « dans le cloud »…)."""

    def __init__(self):
        self.donnees = None

    def ecrire(self, donnees):
        self.donnees = json.loads(json.dumps(donnees))  # copie profonde

    def lire(self):
        return self.donnees
