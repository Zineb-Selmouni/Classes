"""Entraînement 4 · Builder : la forge d'armes sur mesure 

Le forgeron fabrique des épées sur mesure. Le constructeur Epee(...) avait
fini par avoir 8 paramètres optionnels, illisibles à l'appel.
1. Une dataclass immuable Epee(lame, garde, enchantements, degats).
2. Un ForgeBuilder avec une interface fluide :
     ForgeBuilder().lame("acier").garde("dorée").enchanter("feu").enchanter("givre").forger()
   - lames : "fer" (8 dégâts), "acier" (12), "mithril" (18) ;
   - chaque enchantement ajoute 3 dégâts, 3 au maximum (sinon ValueError) ;
   - forger() lève ValueError si aucune lame n'a été choisie ;
   - garde par défaut : "simple".
3. Un « directeur » epee_du_chevalier() qui construit toujours la même épée :
   acier, garde dorée, enchantement « sacré ».
"""


from dataclasses import dataclass

LAMES = {"fer": 8, "acier": 12, "mithril": 18}
BONUS_ENCHANTEMENT = 3
MAX_ENCHANTEMENTS = 3


# TODO : la dataclass Epee(lame, garde, enchantements, degats)


class ForgeBuilder:
    # TODO : lame(), garde(), enchanter(), forger() — chaque méthode renvoie self
    pass


def epee_du_chevalier():
    # TODO
    pass


if __name__ == "__main__":
    e = ForgeBuilder().lame("acier").garde("dorée").enchanter("feu").enchanter("givre").forger()
    assert e == Epee("acier", "dorée", ("feu", "givre"), 18)
    assert ForgeBuilder().lame("fer").forger().garde == "simple"
    assert epee_du_chevalier().degats == 15
    for erreur in (lambda: ForgeBuilder().forger(), lambda: ForgeBuilder().lame("bois"),
                   lambda: ForgeBuilder().lame("fer").enchanter("a").enchanter("b").enchanter("c").enchanter("d")):
        try:
            erreur()
        except ValueError:
            pass
        else:
            raise AssertionError("ValueError attendue")
    print("Tous les tests passent !")
