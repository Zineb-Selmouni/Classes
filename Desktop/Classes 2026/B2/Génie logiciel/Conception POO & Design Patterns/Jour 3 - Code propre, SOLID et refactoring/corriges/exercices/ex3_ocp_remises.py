"""Entraînement 3 · O comme Open/Closed : les remises du marchand (corrigé)

Version « avant » :

    def prix_final(prix, client):
        if client == "normal":
            return prix
        elif client == "membre":
            return prix * 0.9
        elif client == "vip":
            return prix * 0.8 - 5
        # le studio veut un client « légende »… il faut encore modifier ici !

Réécrivez avec une classe abstraite Remise (méthode appliquer(prix)) et
une sous-classe par type de client. La fonction prix_final(prix, remise)
ne doit plus jamais être modifiée. Ajoutez ensuite RemiseLegende
(moitié prix) SANS toucher à prix_final. Le prix ne descend jamais sous 0.
"""
from abc import ABC, abstractmethod


class Remise(ABC):
    @abstractmethod
    def appliquer(self, prix: float) -> float: ...


class AucuneRemise(Remise):
    def appliquer(self, prix):
        return prix


class RemiseMembre(Remise):
    def appliquer(self, prix):
        return prix * 0.9


class RemiseVip(Remise):
    def appliquer(self, prix):
        return prix * 0.8 - 5


class RemiseLegende(Remise):  # ajoutée sans modifier prix_final
    def appliquer(self, prix):
        return prix * 0.5


def prix_final(prix, remise: Remise):
    return max(0, round(remise.appliquer(prix), 2))


if __name__ == "__main__":
    assert prix_final(100, AucuneRemise()) == 100
    assert prix_final(100, RemiseMembre()) == 90
    assert prix_final(100, RemiseVip()) == 75
    assert prix_final(100, RemiseLegende()) == 50
    assert prix_final(3, RemiseVip()) == 0
    print("Tous les tests passent !")
