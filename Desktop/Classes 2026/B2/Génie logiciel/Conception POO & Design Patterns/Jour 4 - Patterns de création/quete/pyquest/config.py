"""Étape 1 — Singleton : une seule Configuration pour toute la partie.

Configuration() renvoie TOUJOURS le même objet (redéfinissez __new__).
- attributs difficulte = "normal" et graine = None à la première création ;
- propriété multiplicateur : 0.75 (facile), 1.0 (normal), 1.5 (difficile) ;
- changer_difficulte(niveau) : ValueError si le niveau est inconnu ;
- classmethod reinitialiser() : oublie l'instance (utile pour les tests).
"""

DIFFICULTES = {"facile": 0.75, "normal": 1.0, "difficile": 1.5}


class Configuration:
    _instance = None

    # TODO
