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
        """L'algorithme, écrit une seule fois :
        preparer() ; puis tant que les deux sont vivants : tour += 1,
        tour_du_hero(), et tour_de_l_adversaire() si le combat continue ;
        enfin renvoyer conclure()."""
        # TODO

    # ------------------------------------------------------------ les étapes
    @abstractmethod
    def preparer(self):
        """Étape obligatoire : chaque rencontre commence à sa façon."""

    def tour_du_hero(self):
        """Si le héros peut agir : capacité spéciale tous les TOUR_CAPACITE tours
        (publiée comme "action"), sinon attaque publiée comme "attaque"."""
        # TODO

    def tour_de_l_adversaire(self):
        """Si l'adversaire peut agir : annoncer adversaire.agir(hero, rng)."""
        # TODO

    def conclure(self):
        """Victoire : publier "victoire", appeler recompenser(), renvoyer le héros.
        Défaite : publier "defaite", renvoyer l'adversaire."""
        # TODO

    def recompenser(self):
        """Crochet (hook) : par défaut, le héros gagne l'XP de l'adversaire.
        Annonces : "+30 XP", puis "Brakk passe au niveau 2 !" s'il monte."""
        # TODO

    # ------------------------------------------------------------ outils internes
    def _combat_en_cours(self):
        return self.hero.est_vivant and self.adversaire.est_vivant

    def _peut_agir(self, perso):
        """Applique l'état du personnage (State) et annonce son message éventuel."""
        peut_agir, message = perso.etat.debut_de_tour(perso)
        if message:
            self._annoncer(message)
        return peut_agir and self._combat_en_cours()

    def _annoncer(self, message):
        self.bus.publier("action", message=message)


# TODO : Duel        -> preparer annonce "Duel : Brakk contre Slime !"
# TODO : Embuscade   -> preparer annonce "Embuscade ! Slime attaque par surprise"
#                       puis l'adversaire joue un tour gratuit
# TODO : Entrainement -> preparer annonce "Entraînement contre Slime"
#                       et recompenser annonce seulement "Pas d'XP à l'entraînement"
