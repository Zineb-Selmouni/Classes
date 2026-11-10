"""Entraînement 5 · Du diagramme au code : le coffre au trésor 

Traduisez le diagramme UML de la diapositive en Python :

    Coffre
    - _verrouille : bool
    - _contenu : list
    + code : str            (en lecture seule)
    + ouvrir(code: str) -> bool
    + fermer() -> None
    + prendre_tout() -> list   (lève PermissionError si verrouillé)
    + est_verrouille -> bool   (propriété)

    Un Coffre contient 0..* objets (ici, des chaînes de caractères).
"""


class Coffre:
    def __init__(self, code, contenu=None):
        # TODO
        pass

    # TODO : propriétés code et est_verrouille, méthodes ouvrir, fermer, prendre_tout


if __name__ == "__main__":
    c = Coffre("1234", ["Rubis", "Clé rouillée"])
    assert c.est_verrouille
    try:
        c.prendre_tout()
    except PermissionError:
        pass
    else:
        raise AssertionError("PermissionError attendue")
    assert c.ouvrir("0000") is False
    assert c.ouvrir("1234") is True
    assert c.prendre_tout() == ["Rubis", "Clé rouillée"]
    assert c.prendre_tout() == []
    c.fermer()
    assert c.est_verrouille
    print("Tous les tests passent !")
