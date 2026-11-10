"""Entraînement 4 · Composite : le sac sans fond 

Un sac d'aventurier peut contenir des objets… et d'autres sacs (une bourse,
un carquois…). On veut traiter un objet et un sac de la même façon.
1. Objet(nom, poids, valeur) : poids() et valeur() renvoient ses valeurs.
2. Sac(nom, poids_vide=0.5) : contient des éléments (Objet ou Sac) ;
   poids() = poids_vide + somme des poids ; valeur() = somme des valeurs.
3. inventaire(indentation=0) renvoie les lignes d'un affichage en arbre :
      Sac à dos (3.5 kg)
        Épée (2.0 kg)
        Bourse (0.6 kg)
          Rubis (0.1 kg)
"""


from abc import ABC, abstractmethod


class Element(ABC):
    def __init__(self, nom):
        self.nom = nom

    # TODO : poids() et valeur() abstraites ; inventaire(indentation) commun


# TODO : Objet(nom, poids, valeur) et Sac(nom, poids_vide=0.5) avec ajouter() (qui renvoie self)


if __name__ == "__main__":
    bourse = Sac("Bourse").ajouter(Objet("Rubis", 0.1, 50))
    sac = Sac("Sac à dos", 0.9).ajouter(Objet("Épée", 2.0, 30)).ajouter(bourse)
    assert round(sac.poids(), 1) == 3.5 and sac.valeur() == 80
    assert sac.inventaire() == ["Sac à dos (3.5 kg)", "  Épée (2.0 kg)", "  Bourse (0.6 kg)", "    Rubis (0.1 kg)"]
    print("Tous les tests passent !")
