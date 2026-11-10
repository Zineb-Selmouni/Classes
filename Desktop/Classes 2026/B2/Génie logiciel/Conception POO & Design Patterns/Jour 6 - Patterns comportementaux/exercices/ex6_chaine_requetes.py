"""Entraînement 6 · Chain of Responsibility : les doléances du royaume 

Une requête (description, gravite de 1 à 10) remonte la hiérarchie jusqu'à
quelqu'un qui peut la traiter :
  Garde     : gravité <= 2
  Capitaine : gravité <= 5
  Roi       : gravité <= 8
Au-delà, personne : "Personne ne peut traiter : <description>".
1. Une classe de base Responsable(suivant=None) avec traiter(requete) :
   si peut_traiter(requete) -> "Garde traite : <description>"
   sinon on passe au suivant (ou on renvoie le message d'échec).
2. Les sous-classes ne définissent QUE leur limite de gravité.
3. Bonus : un Espion qui ne traite rien mais note toutes les requêtes qui
   passent (dans self.vues) avant de les transmettre.
"""


from dataclasses import dataclass


@dataclass
class Requete:
    description: str
    gravite: int


class Responsable:
    limite = 0

    def __init__(self, suivant=None):
        self.suivant = suivant

    # TODO : peut_traiter(requete) et traiter(requete)


# TODO : Garde (2), Capitaine (5), Roi (8)
# Bonus : Espion


if __name__ == "__main__":
    chaine = Garde(Capitaine(Roi()))
    assert chaine.traiter(Requete("Chat dans un arbre", 1)) == "Garde traite : Chat dans un arbre"
    assert chaine.traiter(Requete("Vol au marché", 4)) == "Capitaine traite : Vol au marché"
    assert chaine.traiter(Requete("Dragon aux portes", 8)) == "Roi traite : Dragon aux portes"
    assert chaine.traiter(Requete("Fin du monde", 10)) == "Personne ne peut traiter : Fin du monde"
    espion = Espion(Garde(Roi()))             # on recompose la chaîne librement
    assert espion.traiter(Requete("Vol au marché", 4)) == "Roi traite : Vol au marché"
    assert espion.vues == ["Vol au marché"]
    print("Tous les tests passent !")
