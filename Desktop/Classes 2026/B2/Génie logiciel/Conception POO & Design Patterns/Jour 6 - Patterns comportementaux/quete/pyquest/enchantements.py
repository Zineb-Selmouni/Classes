"""Decorator : enchanter une arme sans créer une classe par combinaison.

Un enchantement « enveloppe » une arme (ou une arme déjà enchantée) et offre
exactement la même interface : nom, degats, critique.
"""


class ArmeDecorateur:
    def __init__(self, arme):
        self._arme = arme

    @property
    def nom(self):
        return self._arme.nom

    @property
    def degats(self):
        return self._arme.degats

    @property
    def critique(self):
        return self._arme.critique

    def __repr__(self):
        return f"{type(self).__name__}({self._arme!r})"


class EnchantementDeFeu(ArmeDecorateur):
    @property
    def nom(self):
        return self._arme.nom + " de feu"

    @property
    def degats(self):
        return self._arme.degats + 4


class EnchantementDeGivre(ArmeDecorateur):
    @property
    def nom(self):
        return self._arme.nom + " de givre"

    @property
    def degats(self):
        return self._arme.degats + 2


class EnchantementAffute(ArmeDecorateur):
    """Augmente les chances de coup critique (sans dépasser 100 %)."""

    @property
    def nom(self):
        return self._arme.nom + " affûtée"

    @property
    def critique(self):
        return min(1.0, self._arme.critique + 0.15)
