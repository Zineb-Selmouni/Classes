"""Entraînement 2 · S comme Single Responsibility : la taverne (corrigé)

La classe TaverneTropOccupee fait tout : elle stocke la commande, calcule le prix
(avec la remise du jour), met en forme la note et « l'envoie ».
Découpez-la en classes qui n'ont chacune qu'UNE raison de changer :
- Commande : les plats commandés (ajouter, lignes) ;
- Tarif : le calcul du total (prix de la carte, remise) ;
- NoteFormatee : la mise en forme du texte de la note ;
- la fonction servir(commande, tarif, formateur) assemble le tout.
"""
from dataclasses import dataclass, field

CARTE = {"ragoût": 8, "pain": 2, "hydromel": 5}


# ------------------------------------------------ AVANT (à ne pas imiter)
class TaverneTropOccupee:
    def __init__(self):
        self.plats = []

    def commander(self, plat, quantite=1):
        self.plats.append((plat, quantite))

    def note(self, remise_pourcent=0):
        total = sum(CARTE[p] * q for p, q in self.plats)
        total = total * (100 - remise_pourcent) // 100
        lignes = [f"{q} x {p} : {CARTE[p] * q} po" for p, q in self.plats]
        lignes.append(f"TOTAL : {total} po")
        return "\n".join(lignes)


# ------------------------------------------------ APRÈS
@dataclass
class Commande:
    lignes: list = field(default_factory=list)

    def ajouter(self, plat, quantite=1):
        if plat not in CARTE:
            raise ValueError(f"{plat} n'est pas à la carte")
        self.lignes.append((plat, quantite))


@dataclass(frozen=True)
class Tarif:
    carte: dict
    remise_pourcent: int = 0

    def prix_ligne(self, plat, quantite):
        return self.carte[plat] * quantite

    def total(self, commande):
        brut = sum(self.prix_ligne(p, q) for p, q in commande.lignes)
        return brut * (100 - self.remise_pourcent) // 100


class NoteFormatee:
    def formater(self, commande, tarif):
        lignes = [f"{q} x {p} : {tarif.prix_ligne(p, q)} po" for p, q in commande.lignes]
        lignes.append(f"TOTAL : {tarif.total(commande)} po")
        return "\n".join(lignes)


def servir(commande, tarif, formateur):
    return formateur.formater(commande, tarif)


if __name__ == "__main__":
    vieille = TaverneTropOccupee()
    vieille.commander("ragoût", 2)
    vieille.commander("hydromel")
    c = Commande()
    c.ajouter("ragoût", 2)
    c.ajouter("hydromel")
    assert servir(c, Tarif(CARTE, 10), NoteFormatee()) == vieille.note(10)
    assert Tarif(CARTE).total(c) == 21
    try:
        c.ajouter("sushi")
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError attendue")
    print("Tous les tests passent !")
