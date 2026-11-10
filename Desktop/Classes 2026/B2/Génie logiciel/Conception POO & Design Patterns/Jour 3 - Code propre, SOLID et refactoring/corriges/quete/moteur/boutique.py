"""La boutique et les potions : des catalogues au lieu de chaînes de if."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Article:
    nom: str
    prix: int
    bonus_attaque: int = 0


CATALOGUE = {a.nom: a for a in [Article("potion", 10), Article("grande potion", 25), Article("epee", 50, bonus_attaque=5)]}

# ordre de priorité : on boit d'abord la plus grande potion
SOINS = {"grande potion": 50, "potion": 20}


class Boutique:
    def __init__(self, affichage, catalogue=CATALOGUE):
        self.affichage = affichage
        self.catalogue = catalogue

    def acheter(self, hero, nom_objet):
        article = self.catalogue.get(nom_objet)
        if article is None:
            self.affichage.afficher("Objet inconnu")
            return False
        prix = article.prix - hero.classe.reduction_boutique
        if hero.or_ < prix:
            self.affichage.afficher("Pas assez d'or !")
            return False
        hero.or_ -= prix
        hero.inventaire.append(article.nom)
        hero.attaque += article.bonus_attaque
        self.affichage.afficher(f"{hero.nom} achète : {article.nom} ({prix} pièces)")
        return True


def boire(hero, affichage):
    for potion, soin in SOINS.items():
        if potion in hero.inventaire:
            hero.inventaire.remove(potion)
            gagnes = hero.soigner(soin)
            affichage.afficher(f"{hero.nom} boit une potion : +{gagnes} PV")
            return gagnes
    affichage.afficher("Aucune potion !")
    return 0
