"""Entraînement 1 · La fabrique de projectiles 

Dans un jeu de tir, le code crée des projectiles avec des if partout :

    if arme == "arc": p = Fleche(...)
    elif arme == "arbalete": p = Carreau(...)
    elif arme == "canon": p = Boulet(...)

1. Écrivez une classe abstraite Projectile (nom, degats, vitesse) et trois sous-classes
   Fleche (10 dégâts, vitesse 30), Carreau (15, 40), Boulet (40, 10).
2. Écrivez une fabrique simple creer_projectile(arme) qui s'appuie sur un registre
   (un dictionnaire arme -> classe), rempli grâce à un décorateur @pour_arme("arc").
3. Une arme inconnue lève ValueError.
4. Ajoutez une Bombe (60, 5) pour l'arme "catapulte" SANS modifier creer_projectile.
"""


from abc import ABC

_REGISTRE = {}


def pour_arme(arme):
    """Décorateur de classe : enregistre la classe pour cette arme dans _REGISTRE."""
    # TODO
    pass


class Projectile(ABC):
    nom = "projectile"
    degats = 0
    vitesse = 0

    def __repr__(self):
        return f"{self.nom}({self.degats} dégâts, vitesse {self.vitesse})"


# TODO : Fleche, Carreau, Boulet (décorées avec @pour_arme), puis Bombe


def creer_projectile(arme):
    # TODO
    pass


if __name__ == "__main__":
    assert isinstance(creer_projectile("arc"), Fleche)
    assert repr(creer_projectile("canon")) == "Boulet(40 dégâts, vitesse 10)"
    assert creer_projectile("catapulte").degats == 60
    assert creer_projectile("arc") is not creer_projectile("arc")
    try:
        creer_projectile("lance-pierre")
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError attendue")
    print("Tous les tests passent !")
