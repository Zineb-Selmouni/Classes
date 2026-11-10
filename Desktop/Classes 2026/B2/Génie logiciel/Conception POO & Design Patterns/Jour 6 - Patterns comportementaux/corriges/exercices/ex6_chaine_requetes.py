"""Entraînement 6 · Chain of Responsibility : les doléances du royaume (corrigé)

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

    def peut_traiter(self, requete):
        return requete.gravite <= self.limite

    def traiter(self, requete):
        if self.peut_traiter(requete):
            return f"{type(self).__name__} traite : {requete.description}"
        if self.suivant is not None:
            return self.suivant.traiter(requete)
        return f"Personne ne peut traiter : {requete.description}"


class Garde(Responsable):
    limite = 2


class Capitaine(Responsable):
    limite = 5


class Roi(Responsable):
    limite = 8


class Espion(Responsable):
    def __init__(self, suivant=None):
        super().__init__(suivant)
        self.vues = []

    def traiter(self, requete):
        self.vues.append(requete.description)
        return super().traiter(requete)       # limite 0 : il transmet toujours


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
