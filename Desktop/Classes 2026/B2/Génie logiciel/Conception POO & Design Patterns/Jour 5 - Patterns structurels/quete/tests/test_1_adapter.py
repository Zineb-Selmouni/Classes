"""Étape 1 — Adapter : le service de scores du partenaire."""
from pyquest.scores import AdaptateurArcadeCloud, ArcadeCloudAPI, TableauEnMemoire


def test_tableau_en_memoire():
    t = TableauEnMemoire()
    for nom, score in [("Aria", 120), ("Bob", 300), ("Zed", 300), ("Lyra", 50)]:
        t.enregistrer(nom, score)
    assert t.meilleurs(3) == [("Bob", 300), ("Zed", 300), ("Aria", 120)]


def test_l_adaptateur_traduit_l_enregistrement():
    api = ArcadeCloudAPI()
    AdaptateurArcadeCloud(api).enregistrer("Aria", 1250)
    assert api._lignes == [{"game": "pyquest", "player": "Aria", "kpoints": 1.25}]


def test_l_adaptateur_traduit_le_classement():
    api = ArcadeCloudAPI()
    tableau = AdaptateurArcadeCloud(api)
    tableau.enregistrer("Aria", 1250)
    tableau.enregistrer("Bob", 400)
    assert tableau.meilleurs(2) == [("Aria", 1250), ("Bob", 400)]


def test_meme_interface_que_le_tableau_en_memoire():
    for tableau in (TableauEnMemoire(), AdaptateurArcadeCloud(ArcadeCloudAPI())):
        tableau.enregistrer("Aria", 10)
        assert tableau.meilleurs(1) == [("Aria", 10)]
