"""Singleton : une seule configuration de partie pour tout le jeu.

Version « classique » avec __new__, pour l'étudier. En Python, un simple
objet créé au niveau d'un module (CONFIG = Configuration()) joue déjà ce
rôle, et l'injection de dépendances est souvent encore préférable.
"""

DIFFICULTES = {"facile": 0.75, "normal": 1.0, "difficile": 1.5}


class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            instance = super().__new__(cls)
            instance.difficulte = "normal"
            instance.graine = None
            cls._instance = instance
        return cls._instance

    @property
    def multiplicateur(self):
        return DIFFICULTES[self.difficulte]

    def changer_difficulte(self, niveau):
        if niveau not in DIFFICULTES:
            raise ValueError(f"Difficulté inconnue : {niveau}")
        self.difficulte = niveau

    @classmethod
    def reinitialiser(cls):
        """Pour les tests : repartir d'une configuration neuve."""
        cls._instance = None
