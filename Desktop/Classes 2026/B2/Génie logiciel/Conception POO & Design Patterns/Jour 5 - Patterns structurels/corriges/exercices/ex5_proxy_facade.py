"""Entraînement 5 · Proxy et Facade : la carte du monde (corrigé)

Partie A — Proxy virtuel (chargement paresseux)
  CarteHD est très lourde à charger (chargements compte les chargements réels).
  1. ProxyCarte(nom) a la même interface (nom, afficher()) mais ne crée la
     CarteHD qu'au premier afficher(), puis la réutilise.

Partie B — Facade
  Pour voyager, il faut aujourd'hui : vérifier l'or, payer le passeur, déplacer
  le héros, charger la carte et l'afficher… 5 objets à coordonner.
  2. AgenceDeVoyage.voyager(hero, destination) fait tout cela en un appel
     et renvoie un message ; sans assez d'or, rien ne change.
"""


class CarteHD:
    chargements = 0

    def __init__(self, nom):
        CarteHD.chargements += 1
        self.nom = nom

    def afficher(self):
        return f"[Carte HD de {self.nom}]"


class ProxyCarte:
    def __init__(self, nom):
        self.nom = nom
        self._carte = None

    def afficher(self):
        if self._carte is None:
            self._carte = CarteHD(self.nom)
        return self._carte.afficher()


class Hero:
    def __init__(self, nom, or_, lieu):
        self.nom, self.or_, self.lieu = nom, or_, lieu


class Passeur:
    TARIFS = {"Port-Lumière": 20, "Montagnes": 35}

    def prix(self, destination):
        return self.TARIFS[destination]


class AgenceDeVoyage:
    def __init__(self):
        self.passeur = Passeur()
        self.cartes = {}

    def voyager(self, hero, destination):
        prix = self.passeur.prix(destination)
        if hero.or_ < prix:
            return f"{hero.nom} n'a pas assez d'or pour aller à {destination}"
        hero.or_ -= prix
        hero.lieu = destination
        carte = self.cartes.setdefault(destination, ProxyCarte(destination))
        return f"{hero.nom} arrive à {destination} {carte.afficher()}"


if __name__ == "__main__":
    p = ProxyCarte("Royaume")
    assert CarteHD.chargements == 0
    p.afficher()
    p.afficher()
    assert CarteHD.chargements == 1

    agence = AgenceDeVoyage()
    aria = Hero("Aria", 50, "Village")
    assert agence.voyager(aria, "Port-Lumière") == "Aria arrive à Port-Lumière [Carte HD de Port-Lumière]"
    assert aria.or_ == 30 and aria.lieu == "Port-Lumière"
    assert agence.voyager(aria, "Montagnes") == "Aria n'a pas assez d'or pour aller à Montagnes"
    assert aria.or_ == 30 and aria.lieu == "Port-Lumière"
    print("Tous les tests passent !")
