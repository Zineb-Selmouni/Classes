"""Template Method : le déroulé d'une rencontre est fixé dans jouer() ;
les sous-classes ne redéfinissent que certaines étapes.

C'est aussi ici que tout se rejoint : les personnages ont un état (State),
les monstres une stratégie (Strategy), et tout est publié sur le bus (Observer).
"""
import random
from abc import ABC, abstractmethod

from .evenements import BusEvenements

TOUR_CAPACITE = 3


class Rencontre(ABC):
    def __init__(self, hero, adversaire, bus=None, rng=random):
        self.hero = hero
        self.adversaire = adversaire
        self.bus = bus or BusEvenements()
        self.rng = rng
        self.tour = 0

    # ------------------------------------------------------------ la méthode modèle
    def jouer(self):
        """L'algorithme, écrit une seule fois. Ne pas redéfinir."""
        self.preparer()
        while self._combat_en_cours():
            self.tour += 1
            self.tour_du_hero()
            if self._combat_en_cours():
                self.tour_de_l_adversaire()
        return self.conclure()

    # ------------------------------------------------------------ les étapes
    @abstractmethod
    def preparer(self):
        """Étape obligatoire : chaque rencontre commence à sa façon."""

    def tour_du_hero(self):
        if not self._peut_agir(self.hero):
            return
        if self.tour % TOUR_CAPACITE == 0:
            self._annoncer(self.hero.capacite_speciale(self.adversaire, self.rng))
        else:
            degats = self.hero.attaquer(self.adversaire, self.rng)
            self.bus.publier("attaque", auteur=self.hero, cible=self.adversaire, degats=degats)

    def tour_de_l_adversaire(self):
        if self._peut_agir(self.adversaire):
            self._annoncer(self.adversaire.agir(self.hero, self.rng))

    def conclure(self):
        if self.hero.est_vivant:
            self.bus.publier("victoire", hero=self.hero, adversaire=self.adversaire)
            self.recompenser()
            return self.hero
        self.bus.publier("defaite", hero=self.hero, adversaire=self.adversaire)
        return self.adversaire

    def recompenser(self):
        """Crochet (hook) : comportement par défaut, que l'on PEUT redéfinir."""
        xp = self.adversaire.xp_donnee
        monte = self.hero.gagner_xp(xp)
        self._annoncer(f"+{xp} XP")
        if monte:
            self._annoncer(f"{self.hero.nom} passe au niveau {self.hero.niveau} !")

    # ------------------------------------------------------------ outils internes
    def _combat_en_cours(self):
        return self.hero.est_vivant and self.adversaire.est_vivant

    def _peut_agir(self, perso):
        peut_agir, message = perso.etat.debut_de_tour(perso)
        if message:
            self._annoncer(message)
        return peut_agir and self._combat_en_cours()

    def _annoncer(self, message):
        self.bus.publier("action", message=message)


class Duel(Rencontre):
    def preparer(self):
        self._annoncer(f"Duel : {self.hero.nom} contre {self.adversaire.nom} !")


class Embuscade(Rencontre):
    def preparer(self):
        self._annoncer(f"Embuscade ! {self.adversaire.nom} attaque par surprise")
        self.tour_de_l_adversaire()


class Entrainement(Rencontre):
    def preparer(self):
        self._annoncer(f"Entraînement contre {self.adversaire.nom}")

    def recompenser(self):
        self._annoncer("Pas d'XP à l'entraînement")
