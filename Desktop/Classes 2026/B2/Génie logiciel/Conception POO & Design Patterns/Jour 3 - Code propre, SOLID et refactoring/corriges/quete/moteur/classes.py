"""Les classes de héros : des données, plus des if. (O de SOLID.)"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ClasseDeHero:
    nom: str
    pv: int
    attaque: int
    crit: float
    armure: int = 0               # dégâts retirés à chaque coup reçu
    reduction_boutique: int = 0   # pièces économisées sur chaque achat


CLASSES = {
    "guerrier": ClasseDeHero("guerrier", pv=130, attaque=9, crit=0.1, armure=2),
    "mage": ClasseDeHero("mage", pv=80, attaque=12, crit=0.05),
    "archer": ClasseDeHero("archer", pv=100, attaque=8, crit=0.3, reduction_boutique=2),
}


def classe_par_nom(nom):
    try:
        return CLASSES[nom]
    except KeyError:
        raise ValueError("classe inconnue : " + nom) from None
