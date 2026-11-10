"""Prototype : créer des variantes de monstres en clonant un modèle déjà configuré."""
import copy

from .personnages import Monstre


class RegistreDePrototypes:
    def __init__(self):
        self._modeles = {}

    def ajouter(self, cle, modele):
        self._modeles[cle] = modele

    def cloner(self, cle, **modifications):
        """Copie profonde du modèle, puis application des modifications."""
        if cle not in self._modeles:
            raise KeyError(f"Aucun prototype « {cle} »")
        clone = copy.deepcopy(self._modeles[cle])
        for attribut, valeur in modifications.items():
            setattr(clone, attribut, valeur)
        if "pv_max" in modifications:
            clone.pv = modifications["pv_max"]
        return clone


def registre_par_defaut():
    registre = RegistreDePrototypes()
    gobelin = Monstre("Gobelin", 35, 6, 25)
    gobelin.butin = ["dague", "pièce"]  # attribut mutable : la copie doit être profonde
    registre.ajouter("gobelin", gobelin)
    registre.ajouter("gobelin d'élite", registre.cloner("gobelin", nom="Gobelin d'élite", pv_max=60, degats=10))
    return registre
