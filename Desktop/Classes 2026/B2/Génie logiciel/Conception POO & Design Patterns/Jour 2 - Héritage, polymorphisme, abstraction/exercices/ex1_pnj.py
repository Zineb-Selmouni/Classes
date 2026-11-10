"""Entraînement 1 · Les PNJ du village 

Les personnages non joueurs (PNJ) du village parlent au héros.
1. Classe PNJ(nom) avec une méthode parler() qui renvoie "Bonjour, je suis <nom>."
2. Marchand(nom, articles) : parler() ajoute "J'ai N articles à vendre."
   à la phrase de PNJ (utilisez super()).
3. Garde(nom) : parler() renvoie "Halte ! On ne passe pas." (redéfinition complète).
4. Aubergiste(nom, prix_chambre) hérite de Marchand avec la liste ["chambre"] :
   parler() ajoute "Une chambre coûte P pièces." à la phrase de Marchand.
5. La fonction visiter(pnjs) renvoie la liste de ce que dit chacun.
"""


class PNJ:
    # TODO
    pass


# TODO : Marchand, Garde, Aubergiste


def visiter(pnjs):
    # TODO
    pass


if __name__ == "__main__":
    village = [PNJ("Tom"), Marchand("Gilda", ["épée", "bouclier"]), Garde("Bors"), Aubergiste("Mia", 5)]
    assert visiter(village) == [
        "Bonjour, je suis Tom.",
        "Bonjour, je suis Gilda. J'ai 2 articles à vendre.",
        "Halte ! On ne passe pas.",
        "Bonjour, je suis Mia. J'ai 1 articles à vendre. Une chambre coûte 5 pièces.",
    ]
    assert isinstance(village[3], Marchand) and isinstance(village[3], PNJ)
    assert Aubergiste.__mro__ == (Aubergiste, Marchand, PNJ, object)
    print("Tous les tests passent !")
