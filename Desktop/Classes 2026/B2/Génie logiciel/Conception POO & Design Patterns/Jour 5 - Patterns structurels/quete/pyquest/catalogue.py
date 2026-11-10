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
    """Étape 4a — Proxy de cache : même méthode fiche(monstre), un seul appel au catalogue par fiche."""

    # TODO


class CatalogueProtege:
    """Étape 4b — Proxy de protection : CatalogueProtege(catalogue, hero).
    Les fiches de SECRETES demandent un niveau minimal, sinon PermissionError."""

    SECRETES = {"dragon": 5}

    # TODO
