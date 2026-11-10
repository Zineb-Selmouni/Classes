"""Proxy : un intermédiaire qui contrôle l'accès à un objet coûteux.

Ici, un proxy de cache devant le catalogue « distant » des fiches de monstres
(imaginez un serveur lent), et un proxy de protection pour les fiches secrètes.
"""


class CatalogueDistant:
    """Le vrai sujet : lent (chaque appel coûte une requête réseau)."""

    FICHES = {
        "slime": "Masse gélatineuse. Faible contre le feu.",
        "gobelin": "Petit, rusé, voleur. Attaque en groupe.",
        "roi gobelin": "Chef des gobelins. S'enrage quand il est blessé.",
        "dragon": "SECRET : point faible sous l'aile gauche.",
    }

    def __init__(self):
        self.requetes = 0

    def fiche(self, monstre):
        self.requetes += 1  # on simule le coût d'un appel réseau
        if monstre not in self.FICHES:
            raise KeyError(f"Aucune fiche pour {monstre}")
        return self.FICHES[monstre]


class CatalogueEnCache:
    """Proxy de cache : même interface, mais ne dérange le serveur qu'une fois par fiche."""

    def __init__(self, catalogue):
        self._catalogue = catalogue
        self._cache = {}

    def fiche(self, monstre):
        if monstre not in self._cache:
            self._cache[monstre] = self._catalogue.fiche(monstre)
        return self._cache[monstre]


class CatalogueProtege:
    """Proxy de protection : les fiches secrètes demandent un niveau minimal."""

    SECRETES = {"dragon": 5}

    def __init__(self, catalogue, hero):
        self._catalogue = catalogue
        self._hero = hero

    def fiche(self, monstre):
        niveau_requis = self.SECRETES.get(monstre, 0)
        if self._hero.niveau < niveau_requis:
            raise PermissionError(f"Niveau {niveau_requis} requis pour lire la fiche de {monstre}")
        return self._catalogue.fiche(monstre)
