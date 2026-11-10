"""Strategy : le comportement d'un monstre en combat est un objet interchangeable.

Le monstre ne sait pas COMMENT il se bat : il délègue à sa stratégie.

À faire aussi :
  - personnages.py : Monstre(nom, pv, degats, xp_donnee, strategie=None)
    (Agressive() par défaut) et une méthode agir(cible, rng) qui délègue ;
  - groupes.py : GroupeDeMonstres.agir(cible, rng) -> messages des membres
    vivants joints par " / " ;
  - fabriques.py : gobelin Prudente(), roi gobelin Ecrasante(),
    et une nouvelle recette "araignée" (Araignée géante) avec Venimeuse().
"""
import random
from typing import Protocol

from .etats import Empoisonne, Etourdi, Normal  # noqa: F401


class StrategieDeCombat(Protocol):
    def agir(self, monstre, cible, rng) -> str: ...


class Agressive:
    """Exemple fourni : attaque à chaque tour."""

    def agir(self, monstre, cible, rng=random):
        degats = monstre.attaquer(cible, rng)
        return f"{monstre.nom} inflige {degats} dégâts à {cible.nom}"


# TODO : Prudente(seuil=0.3, soin=10, potions=1)
#   sous seuil × pv_max (et s'il reste une potion) : se soigne
#   -> "Gobelin boit une potion : +10 PV" ; sinon attaque comme Agressive


# TODO : Venimeuse(chance=0.3)
#   attaque ; si la cible est dans l'état Normal et rng.random() < chance,
#   elle devient Empoisonne() et le message se termine par " et l'empoisonne"


# TODO : Ecrasante(tous_les=3)
#   attaque ; toutes les `tous_les` attaques, la cible devient Etourdi()
#   et le message se termine par " et l'étourdit"


# TODO : Imprevisible(*strategies)
#   choisit une stratégie avec rng.choice à chaque tour
