"""Entraînement 5 · L'écurie : de l'héritage à la composition 

Le studio veut des montures qui peuvent voler, nager et/ou courir vite.
Un développeur a commencé par l'héritage : Monture, MontureVolante,
MontureNageuse, MontureVolanteNageuse, MontureVolanteRapide… 2^3 = 8 classes
pour 3 capacités, 16 pour 4 : c'est l'explosion combinatoire.

Refaites la conception par composition :
1. Une classe Capacite(nom, bonus_vitesse) ;
2. Une seule classe Monture(nom, vitesse_de_base, capacites=()) qui A des capacités ;
3. vitesse() = vitesse de base + somme des bonus ;
4. peut(nom_capacite) -> bool ;
5. ajouter_capacite(capacite) : une monture peut apprendre en cours de jeu
   (impossible avec l'héritage : un objet ne change pas de classe !).
"""


from dataclasses import dataclass


@dataclass(frozen=True)
class Capacite:
    nom: str
    bonus_vitesse: int = 0


VOL = Capacite("voler", 20)
NAGE = Capacite("nager", 5)
SPRINT = Capacite("sprinter", 15)


class Monture:
    def __init__(self, nom, vitesse_de_base, capacites=()):
        # TODO : la monture A une liste de capacités
        pass

    # TODO : vitesse(), peut(nom_capacite), ajouter_capacite(capacite)


if __name__ == "__main__":
    griffon = Monture("Griffon", 30, [VOL, SPRINT])
    assert griffon.vitesse() == 65 and griffon.peut("voler") and not griffon.peut("nager")
    hippocampe = Monture("Hippocampe", 20, [NAGE])
    assert hippocampe.vitesse() == 25
    poney = Monture("Poney", 10)
    poney.ajouter_capacite(VOL)
    poney.ajouter_capacite(VOL)
    assert poney.peut("voler") and poney.vitesse() == 30
    print("Tous les tests passent !")
