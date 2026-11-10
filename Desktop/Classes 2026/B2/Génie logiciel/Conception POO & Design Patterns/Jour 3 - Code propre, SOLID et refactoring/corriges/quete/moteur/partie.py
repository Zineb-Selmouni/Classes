"""La Partie refactorisée : même interface publique que l'ancienne, mais elle
ne fait plus que coordonner des objets spécialisés, reçus par injection."""
import random

from .affichage import AffichageConsole
from .boutique import Boutique, boire
from .classes import classe_par_nom
from .combat import Combat
from .hero import Hero
from .monstres import creer_monstre
from .stockage import StockageFichier
from .succes import VerificateurDeSucces


class Partie:
    def __init__(self, nom, classe, *, affichage=None, stockage=None, rng=random):
        self.affichage = affichage or AffichageConsole()
        self.stockage = stockage or StockageFichier()
        self.hero = Hero(nom, classe_par_nom(classe))
        self.combat = Combat(self.affichage, rng)
        self.boutique = Boutique(self.affichage)
        self.succes_du_jeu = VerificateurDeSucces(self.affichage)

    # ---- raccourcis de lecture, pour garder l'interface de l'ancienne Partie
    def __getattr__(self, nom):
        """Délègue la lecture d'un attribut inconnu au héros (p.pv, p.niveau…)."""
        if nom == "hero":
            raise AttributeError(nom)
        return getattr(self.hero, nom)

    # ---- actions
    def creer_monstre(self, type_monstre):
        return creer_monstre(type_monstre)

    def combattre(self, type_monstre):
        gagne = self.combat.executer(self.hero, creer_monstre(type_monstre))
        if gagne:
            self.succes_du_jeu.verifier(self.hero)
        return gagne

    def acheter(self, objet):
        return self.boutique.acheter(self.hero, objet)

    def boire(self):
        return boire(self.hero, self.affichage)

    def sauvegarder(self):
        self.stockage.ecrire(self.hero.vers_dict())
        self.affichage.afficher("Partie sauvegardée")

    def charger(self):
        self.hero = Hero.depuis_dict(self.stockage.lire())
        self.affichage.afficher("Partie chargée")

    def afficher(self):
        self.affichage.afficher(self.hero.resume())
