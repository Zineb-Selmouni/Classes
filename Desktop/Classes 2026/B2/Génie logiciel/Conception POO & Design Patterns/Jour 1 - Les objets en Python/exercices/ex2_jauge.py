"""Entraînement 2 · La jauge de mana 

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
        # TODO : stocker le maximum dans un attribut protégé, la valeur démarre au maximum
        pass

    # TODO : propriété maximum (lecture seule)

    # TODO : propriété valeur + setter qui borne entre 0 et maximum

    # TODO : propriétés calculées pourcentage et est_vide

    def __str__(self):
        # TODO : "[######----] 60/100"
        pass


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
