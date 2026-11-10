"""Entraînement 2 · S comme Single Responsibility : la taverne 

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
# TODO : Commande, Tarif, NoteFormatee et la fonction servir(commande, tarif, formateur)


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
