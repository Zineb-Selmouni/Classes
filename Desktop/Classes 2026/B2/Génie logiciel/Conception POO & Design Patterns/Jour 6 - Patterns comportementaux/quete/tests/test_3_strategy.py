"""Étape 3 · Strategy : strategies.py (et Monstre.agir)"""
from pyquest.etats import Empoisonne, Etourdi
from pyquest.fabriques import creer_monstre
from pyquest.groupes import GroupeDeMonstres
from pyquest.personnages import Guerrier, Monstre
from pyquest.strategies import Agressive, Ecrasante, Imprevisible, Prudente, Venimeuse


class De:
    """Faux hasard : random() renvoie toujours la même valeur, choice() le premier."""

    def __init__(self, valeur):
        self.valeur = valeur

    def random(self):
        return self.valeur

    def choice(self, options):
        return options[0]


def test_un_monstre_est_agressif_par_defaut():
    loup, hero = Monstre("Loup", 30, 5, 10), Guerrier("Brakk")
    assert isinstance(loup.strategie, Agressive)
    assert loup.agir(hero, De(0.9)) == "Loup inflige 5 dégâts à Brakk"
    assert hero.pv == 125


def test_la_strategie_prudente_boit_sa_potion_une_seule_fois():
    gobelin, hero = Monstre("Gobelin", 30, 5, 10, Prudente(seuil=0.5, soin=10)), Guerrier("Brakk")
    gobelin.pv = 10
    assert gobelin.agir(hero, De(0.9)) == "Gobelin boit une potion : +10 PV"
    assert gobelin.pv == 20 and hero.pv == hero.pv_max
    gobelin.pv = 5
    assert "inflige" in gobelin.agir(hero, De(0.9))      # plus de potion : il attaque


def test_la_strategie_venimeuse_empoisonne():
    araignee, hero = Monstre("Araignée", 20, 3, 10, Venimeuse(chance=0.5)), Guerrier("Brakk")
    assert araignee.agir(hero, De(0.9)).endswith("Brakk")          # 0.9 > 0.5 : pas de poison
    assert araignee.agir(hero, De(0.1)).endswith("et l'empoisonne")
    assert isinstance(hero.etat, Empoisonne)


def test_on_peut_changer_de_strategie_en_cours_de_combat():
    loup, hero = Monstre("Loup", 30, 5, 10), Guerrier("Brakk")
    loup.strategie = Venimeuse(chance=1.0)
    assert loup.agir(hero, De(0.9)).endswith("et l'empoisonne")


def test_imprevisible_compose_des_strategies():
    loup, hero = Monstre("Loup", 30, 5, 10, Imprevisible(Venimeuse(1.0), Agressive())), Guerrier("Brakk")
    assert loup.agir(hero, De(0.0)).endswith("et l'empoisonne")    # De.choice prend la 1re


def test_les_fabriques_donnent_des_strategies_aux_monstres():
    assert isinstance(creer_monstre("araignée").strategie, Venimeuse)
    assert isinstance(creer_monstre("gobelin").strategie, Prudente)


def test_un_groupe_agit_avec_la_strategie_de_chaque_membre():
    bande = GroupeDeMonstres("Bande", [Monstre("A", 10, 2, 5), Monstre("B", 10, 3, 5)])
    hero = Guerrier("Brakk")
    assert bande.agir(hero, De(0.9)) == "A inflige 2 dégâts à Brakk / B inflige 3 dégâts à Brakk"


def test_la_strategie_ecrasante_etourdit_toutes_les_3_attaques():
    roi, hero = Monstre("Roi", 80, 5, 50, Ecrasante()), Guerrier("Brakk")
    messages = [roi.agir(hero, De(0.9)) for _ in range(3)]
    assert not messages[1].endswith("étourdit") and messages[2].endswith("et l'étourdit")
    assert isinstance(hero.etat, Etourdi)
