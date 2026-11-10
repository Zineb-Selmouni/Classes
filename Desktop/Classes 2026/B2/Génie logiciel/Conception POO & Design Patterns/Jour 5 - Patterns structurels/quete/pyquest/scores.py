"""Adapter : brancher le service de scores d'un partenaire sur NOTRE interface."""
from typing import Protocol


class TableauDesScores(Protocol):
    """L'interface dont notre jeu a besoin."""

    def enregistrer(self, nom: str, score: int) -> None: ...
    def meilleurs(self, n: int = 3) -> list: ...


class TableauEnMemoire:
    """Étape 1a — enregistrer(nom, score) ; meilleurs(n) trié par score décroissant, puis par nom."""

    # TODO


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
    """Étape 1b — Adapter : AdaptateurArcadeCloud(api, jeu="pyquest") respecte TableauDesScores.
    enregistrer(nom, score) -> api.submit({"game": jeu, "player": nom, "kpoints": score / 1000})
    meilleurs(n) -> [(player, points entiers), …] à partir de api.leaderboard(n)."""

    # TODO
