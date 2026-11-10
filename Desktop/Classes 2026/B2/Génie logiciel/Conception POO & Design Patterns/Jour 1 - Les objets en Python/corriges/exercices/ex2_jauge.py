"""Entraînement 2 · La jauge de mana (corrigé)

Créez une classe Jauge(maximum) :
- la valeur démarre au maximum ;
- la propriété valeur est bornée entre 0 et maximum (jamais d'erreur, on « coupe ») ;
- la propriété maximum est en lecture seule ;
- la propriété calculée pourcentage renvoie un entier entre 0 et 100 ;
- la propriété est_vide renvoie True quand la valeur vaut 0 ;
- __str__ affiche une barre : [######----] 60/100
"""


class Jauge:
    def __init__(self, maximum):
        if maximum <= 0:
            raise ValueError("Le maximum doit être positif")
        self._maximum = maximum
        self._valeur = maximum

    @property
    def maximum(self):
        return self._maximum

    @property
    def valeur(self):
        return self._valeur

    @valeur.setter
    def valeur(self, v):
        self._valeur = max(0, min(v, self._maximum))

    @property
    def pourcentage(self):
        return round(100 * self._valeur / self._maximum)

    @property
    def est_vide(self):
        return self._valeur == 0

    def __str__(self):
        pleins = self.pourcentage // 10
        return "[" + "#" * pleins + "-" * (10 - pleins) + f"] {self._valeur}/{self._maximum}"


if __name__ == "__main__":
    mana = Jauge(100)
    assert mana.valeur == 100
    mana.valeur -= 40
    assert mana.valeur == 60 and mana.pourcentage == 60
    assert str(mana) == "[######----] 60/100"
    mana.valeur = 500
    assert mana.valeur == 100
    mana.valeur = -3
    assert mana.est_vide
    try:
        mana.maximum = 200
    except AttributeError:
        pass
    else:
        raise AssertionError("maximum doit être en lecture seule")
    print("Tous les tests passent !")
