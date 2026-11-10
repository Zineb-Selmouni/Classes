"""Entraînement 1 · La chasse aux code smells 

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


Votre liste de smells (à compléter) :
 1.
"""


def rapport_guilde(l):
    # Version « avant » : réécrivez-la proprement (Membre, constantes, table de bonus…)
    # Attention : les tests appellent rapport_guilde avec des objets Membre(nom, classe, niveau)
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
        r = r + m[0] + " : " + str(p) + " points\n"
    if len(l) > 0:
        r = r + "Moyenne : " + str(round(t / len(l), 1)) + "\n"
    if t > 300:
        r = r + "Rang : or"
    elif t > 150:
        r = r + "Rang : argent"
    else:
        r = r + "Rang : bronze"
    return r


# TODO : une dataclass Membre(nom, classe, niveau) avec une méthode points()


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
