"""Entraînement 5 · Du diagramme au code : le coffre au trésor (corrigé)

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
        self._code = code
        self._verrouille = True
        self._contenu = list(contenu or [])

    @property
    def code(self):
        return self._code

    @property
    def est_verrouille(self):
        return self._verrouille

    def ouvrir(self, code):
        if code == self._code:
            self._verrouille = False
        return not self._verrouille

    def fermer(self):
        self._verrouille = True

    def prendre_tout(self):
        if self._verrouille:
            raise PermissionError("Le coffre est verrouillé")
        butin, self._contenu = self._contenu, []
        return butin


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
