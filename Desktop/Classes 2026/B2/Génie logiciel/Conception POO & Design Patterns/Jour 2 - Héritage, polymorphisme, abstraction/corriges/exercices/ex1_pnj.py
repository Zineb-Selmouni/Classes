"""Entraînement 1 · Les PNJ du village (corrigé)

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
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return f"Bonjour, je suis {self.nom}."


class Marchand(PNJ):
    def __init__(self, nom, articles):
        super().__init__(nom)
        self.articles = list(articles)

    def parler(self):
        return super().parler() + f" J'ai {len(self.articles)} articles à vendre."


class Garde(PNJ):
    def parler(self):
        return "Halte ! On ne passe pas."


class Aubergiste(Marchand):
    def __init__(self, nom, prix_chambre):
        super().__init__(nom, ["chambre"])
        self.prix_chambre = prix_chambre

    def parler(self):
        return super().parler() + f" Une chambre coûte {self.prix_chambre} pièces."


def visiter(pnjs):
    return [p.parler() for p in pnjs]


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
