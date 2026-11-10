"""Entraînement 1 · La chasse aux code smells (corrigé)

La fonction rapport_guilde ci-dessous (version « avant », gardée en commentaire)
contient au moins 7 défauts. Listez-les, puis réécrivez-la proprement.
Le comportement (le texte renvoyé) ne doit PAS changer : les tests le vérifient.

AVANT :

    def rapport_guilde(l):
        t = 0
        r = ""
        for m in l:
            if m[1] == "guerrier":
                p = m[2] * 10 + 50
            elif m[1] == "mage":
                p = m[2] * 10 + 30
            elif m[1] == "archer":
                p = m[2] * 10 + 40
            t = t + p
            r = r + m[0] + " : " + str(p) + " points\\n"
        if len(l) > 0:
            r = r + "Moyenne : " + str(round(t / len(l), 1)) + "\\n"
        if t > 300:
            r = r + "Rang : or"
        elif t > 150:
            r = r + "Rang : argent"
        else:
            r = r + "Rang : bronze"
        return r

Les 7 smells :
 1. Noms d'une lettre (l, t, r, m, p) : illisible.
 2. Données « magiques » par position : m[0], m[1], m[2] au lieu d'objets nommés.
 3. if/elif sur un type (la classe) : à remplacer par une table ou du polymorphisme.
 4. Nombres magiques : 10, 50, 30, 40, 300, 150.
 5. Duplication : « m[2] * 10 + … » répété trois fois.
 6. Fonction qui fait tout : calcul des points, moyenne, rang ET mise en forme du texte.
 7. Cas oublié : une classe inconnue fait planter (p non défini) avec un message obscur.
"""
from dataclasses import dataclass

POINTS_PAR_NIVEAU = 10
BONUS_DE_CLASSE = {"guerrier": 50, "mage": 30, "archer": 40}
RANGS = [(300, "or"), (150, "argent"), (0, "bronze")]  # seuil strictement dépassé


@dataclass(frozen=True)
class Membre:
    nom: str
    classe: str
    niveau: int

    def points(self):
        if self.classe not in BONUS_DE_CLASSE:
            raise ValueError(f"Classe inconnue : {self.classe}")
        return self.niveau * POINTS_PAR_NIVEAU + BONUS_DE_CLASSE[self.classe]


def rang(total):
    for seuil, nom in RANGS:
        if total > seuil:
            return nom
    return RANGS[-1][1]


def rapport_guilde(membres):
    lignes = [f"{m.nom} : {m.points()} points" for m in membres]
    total = sum(m.points() for m in membres)
    if membres:
        lignes.append(f"Moyenne : {round(total / len(membres), 1)}")
    lignes.append(f"Rang : {rang(total)}")
    return "\n".join(lignes)


if __name__ == "__main__":
    guilde = [Membre("Brakk", "guerrier", 5), Membre("Lyra", "mage", 7), Membre("Sylas", "archer", 4)]
    assert rapport_guilde(guilde) == "Brakk : 100 points\nLyra : 100 points\nSylas : 80 points\nMoyenne : 93.3\nRang : argent"
    assert rapport_guilde([]) == "Rang : bronze"
    assert rapport_guilde([Membre("A", "guerrier", 30)]).endswith("Rang : or")
    try:
        Membre("X", "barde", 1).points()
    except ValueError as e:
        assert "barde" in str(e)
    else:
        raise AssertionError("ValueError attendue")
    print("Tous les tests passent !")
