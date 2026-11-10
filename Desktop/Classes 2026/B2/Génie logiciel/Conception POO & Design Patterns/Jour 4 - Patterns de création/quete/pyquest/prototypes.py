"""Étape 6 — Prototype : cloner des monstres déjà configurés."""
import copy

from .personnages import Monstre


class RegistreDePrototypes:
    """ajouter(cle, modele) ; cloner(cle, **modifications) -> copie PROFONDE modifiée.
    KeyError si la clé est inconnue. Si pv_max est modifié, pv suit."""

    # TODO


def registre_par_defaut():
    """Un « gobelin » (35 PV, 6 dégâts, 25 XP, butin ["dague", "pièce"])
    et un « gobelin d'élite » cloné depuis lui (nom, pv_max=60, degats=10)."""
    # TODO
