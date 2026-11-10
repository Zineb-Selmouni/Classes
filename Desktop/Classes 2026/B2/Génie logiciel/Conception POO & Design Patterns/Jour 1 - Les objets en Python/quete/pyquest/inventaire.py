"""Le sac du héros."""


class InventairePleinError(Exception):
    """Levée quand on ajoute un objet dans un inventaire plein."""


class Inventaire:
    """Étape 2 — un inventaire à capacité limitée.

    - ajouter(objet) : lève InventairePleinError si l'inventaire est plein
    - retirer(objet) : lève ValueError si l'objet est absent, sinon le renvoie
    - len(inv), objet in inv, for objet in inv doivent fonctionner
    - str(inv) : "Inventaire vide" ou "Inventaire : Potion, Clé"
    """

    def __init__(self, capacite=5):
        self.capacite = capacite
        self._objets = []

    # TODO : ajouter, retirer, __len__, __contains__, __iter__, __str__
