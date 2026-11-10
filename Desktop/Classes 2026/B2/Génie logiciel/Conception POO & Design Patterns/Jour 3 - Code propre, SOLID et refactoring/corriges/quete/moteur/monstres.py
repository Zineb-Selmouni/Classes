"""Le bestiaire. Ajouter un monstre = ajouter une ligne, sans toucher au reste."""
from dataclasses import dataclass, replace


@dataclass
class Monstre:
    nom: str
    pv: int
    attaque: int
    xp: int
    or_: int

    @property
    def est_vivant(self):
        return self.pv > 0


BESTIAIRE = {
    "slime": Monstre("Slime", pv=20, attaque=3, xp=10, or_=5),
    "gobelin": Monstre("Gobelin", pv=35, attaque=6, xp=25, or_=12),
    "orc": Monstre("Orc", pv=60, attaque=10, xp=50, or_=30),
    "dragon": Monstre("Dragon", pv=200, attaque=25, xp=500, or_=300),
}


def creer_monstre(type_monstre):
    """Renvoie un NOUVEAU monstre (copie du modèle du bestiaire)."""
    try:
        return replace(BESTIAIRE[type_monstre])
    except KeyError:
        raise ValueError("monstre inconnu : " + type_monstre) from None
