"""Builder : construire un héros pas à pas, avec validation à la fin."""
from .objets import Arme
from .personnages import Archer, Guerrier, Mage

CLASSES = {"guerrier": Guerrier, "mage": Mage, "archer": Archer}


class HeroBuilder:
    def __init__(self):
        self._nom = None
        self._classe = None
        self._arme = None
        self._objets = []
        self._niveau = 1

    def nomme(self, nom):
        self._nom = nom
        return self  # interface fluide : on peut enchaîner les appels

    def de_classe(self, classe):
        if classe not in CLASSES:
            raise ValueError(f"Classe inconnue : {classe}")
        self._classe = classe
        return self

    def arme(self, arme):
        self._arme = arme
        return self

    def avec(self, objet):
        self._objets.append(objet)
        return self

    def au_niveau(self, niveau):
        self._niveau = niveau
        return self

    def construire(self):
        if not self._nom:
            raise ValueError("Un héros doit avoir un nom")
        if not self._classe:
            raise ValueError("Un héros doit avoir une classe")
        hero = CLASSES[self._classe](self._nom, self._arme)
        for objet in self._objets:
            hero.inventaire.ajouter(objet)
        if self._niveau > 1:
            hero.gagner_xp((self._niveau - 1) * 100)
        return hero


def hero_de_depart(nom, classe):
    """Un « directeur » : une recette standard qui utilise le builder."""
    from .objets import Potion
    armes = {"guerrier": Arme("Épée rouillée", 6), "mage": Arme("Bâton de chêne", 3), "archer": Arme("Arc court", 5, critique=0.1)}
    return HeroBuilder().nomme(nom).de_classe(classe).arme(armes[classe]).avec(Potion("Petite potion", 20)).construire()
