"""Le sac du héros."""


class InventairePleinError(Exception):
    """Levée quand on ajoute un objet dans un inventaire plein."""


class Inventaire:
    def __init__(self, capacite=5):
        self.capacite = capacite
        self._objets = []

    def ajouter(self, objet):
        if len(self) >= self.capacite:
            raise InventairePleinError(f"Inventaire plein ({self.capacite} objets max)")
        self._objets.append(objet)

    def retirer(self, objet):
        if objet not in self:
            raise ValueError(f"{objet.nom} n'est pas dans l'inventaire")
        self._objets.remove(objet)
        return objet

    def __len__(self):
        return len(self._objets)

    def __contains__(self, objet):
        return objet in self._objets

    def __iter__(self):
        return iter(self._objets)

    def __str__(self):
        if not self._objets:
            return "Inventaire vide"
        return "Inventaire : " + ", ".join(o.nom for o in self._objets)
