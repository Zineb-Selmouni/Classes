"""Fabriques de monstres : registre (fabrique simple) et Abstract Factory par biome."""
from abc import ABC, abstractmethod

from .config import Configuration
from .objets import Parchemin, Potion
from .personnages import Boss, Monstre
from .strategies import Ecrasante, Prudente, Venimeuse

# ====================================================================== fabrique simple + registre
_RECETTES = {}


def enregistrer(type_monstre):
    """Décorateur : ajoute une recette de monstre au registre (ouvert à l'extension)."""
    def decorer(fonction):
        _RECETTES[type_monstre] = fonction
        return fonction
    return decorer


@enregistrer("slime")
def _slime(niveau):
    return Monstre("Slime", 15 + 5 * niveau, 2 + niveau, 10 * niveau)


@enregistrer("gobelin")
def _gobelin(niveau):
    return Monstre("Gobelin", 25 + 8 * niveau, 4 + niveau, 20 * niveau, Prudente())


@enregistrer("roi gobelin")
def _roi_gobelin(niveau):
    return Boss("Roi Gobelin", 60 + 20 * niveau, 6 + 2 * niveau, 80 * niveau, Ecrasante())


@enregistrer("araignée")
def _araignee(niveau):
    return Monstre("Araignée géante", 20 + 6 * niveau, 3 + niveau, 25 * niveau, Venimeuse())


def types_connus():
    return sorted(_RECETTES)


def creer_monstre(type_monstre, niveau=1):
    """Crée un monstre adapté au niveau ET à la difficulté de la configuration."""
    if type_monstre not in _RECETTES:
        raise ValueError(f"Monstre inconnu : {type_monstre}")
    monstre = _RECETTES[type_monstre](niveau)
    facteur = Configuration().multiplicateur
    monstre.pv_max = monstre.pv = round(monstre.pv_max * facteur)
    monstre.degats = max(1, round(monstre.degats * facteur))
    return monstre


# ====================================================================== Abstract Factory
class FabriqueDeBiome(ABC):
    """Une famille d'objets cohérents : monstre, trésor et nom de lieu d'un même biome."""

    nom = "biome"

    @abstractmethod
    def creer_monstre(self, niveau) -> Monstre: ...

    @abstractmethod
    def creer_tresor(self): ...

    @abstractmethod
    def decrire_lieu(self) -> str: ...


class FabriqueForet(FabriqueDeBiome):
    nom = "forêt"

    def creer_monstre(self, niveau):
        return Monstre("Loup sauvage", 20 + 6 * niveau, 4 + niveau, 15 * niveau)

    def creer_tresor(self):
        return Potion("Sève de chêne", 30)

    def decrire_lieu(self):
        return "Une clairière silencieuse, éclairée par la lune."


class FabriqueVolcan(FabriqueDeBiome):
    nom = "volcan"

    def creer_monstre(self, niveau):
        return Monstre("Salamandre", 30 + 8 * niveau, 6 + 2 * niveau, 25 * niveau)

    def creer_tresor(self):
        return Parchemin("Parchemin de lave", 30)

    def decrire_lieu(self):
        return "Une caverne brûlante où coule la lave."


def generer_rencontre(fabrique: FabriqueDeBiome, niveau=1):
    """Le code client ne connaît que l'interface : il ne sait pas dans quel biome il est."""
    return {"lieu": fabrique.decrire_lieu(), "monstre": fabrique.creer_monstre(niveau), "tresor": fabrique.creer_tresor()}
