"""Entraînement 2 · Decorator : les boissons de la taverne 

La taverne sert des boissons de base, et des suppléments qu'on peut cumuler.
Créer une classe par combinaison (ThéAuLaitAvecMiel…) serait une explosion.
1. Une classe abstraite Boisson avec description() -> str et prix() -> float.
2. Les boissons de base : The (2.0) et Hydromel (4.5).
3. Un décorateur abstrait Supplement qui enveloppe une Boisson, et trois suppléments :
   Lait (+0.5, « au lait »), Miel (+0.8, « au miel »), Epices (+1.0, « aux épices »).
4. On peut empiler : Miel(Lait(The())) -> « Thé au lait au miel », 3.3.
"""


from abc import ABC, abstractmethod


# TODO : Boisson (abstraite), The, Hydromel, Supplement (enveloppe une Boisson), Lait, Miel, Epices


if __name__ == "__main__":
    b = Miel(Lait(The()))
    assert b.description() == "Thé au lait au miel" and b.prix() == 3.3
    h = Epices(Epices(Hydromel()))
    assert h.description() == "Hydromel aux épices aux épices" and h.prix() == 6.5
    assert isinstance(b, Boisson)
    print("Tous les tests passent !")
