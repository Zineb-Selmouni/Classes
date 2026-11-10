"""Adapter : brancher le service de scores d'un partenaire sur NOTRE interface."""
from typing import Protocol


class TableauDesScores(Protocol):
    """L'interface dont notre jeu a besoin."""

    def enregistrer(self, nom: str, score: int) -> None: ...
    def meilleurs(self, n: int = 3) -> list: ...


class TableauEnMemoire:
    def __init__(self):
        self._scores = []

    def enregistrer(self, nom, score):
        self._scores.append((nom, score))

    def meilleurs(self, n=3):
        return sorted(self._scores, key=lambda e: (-e[1], e[0]))[:n]


class ArcadeCloudAPI:
    """Bibliothèque d'un partenaire : on ne peut PAS la modifier.
    Son interface est différente : identifiants de joueurs, points en milliers, JSON…"""

    def __init__(self):
        self._lignes = []
        self.nb_appels = 0

    def submit(self, payload: dict) -> dict:
        self.nb_appels += 1
        self._lignes.append(dict(payload))
        return {"status": "ok", "rank": None}

    def leaderboard(self, limit: int) -> list:
        self.nb_appels += 1
        tries = sorted(self._lignes, key=lambda l: (-l["kpoints"], l["player"]))
        return [{"player": l["player"], "kpoints": l["kpoints"]} for l in tries[:limit]]


class AdaptateurArcadeCloud:
    """Adapter : présente l'API du partenaire avec l'interface TableauDesScores."""

    def __init__(self, api: ArcadeCloudAPI, jeu="pyquest"):
        self._api = api
        self._jeu = jeu

    def enregistrer(self, nom, score):
        self._api.submit({"game": self._jeu, "player": nom, "kpoints": score / 1000})

    def meilleurs(self, n=3):
        return [(ligne["player"], round(ligne["kpoints"] * 1000)) for ligne in self._api.leaderboard(n)]
