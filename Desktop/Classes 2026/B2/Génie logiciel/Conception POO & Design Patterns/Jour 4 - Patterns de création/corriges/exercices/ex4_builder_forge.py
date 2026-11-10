"""Entraînement 4 · Builder : la forge d'armes sur mesure (corrigé)

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


@dataclass(frozen=True)
class Epee:
    lame: str
    garde: str
    enchantements: tuple
    degats: int


class ForgeBuilder:
    def __init__(self):
        self._lame = None
        self._garde = "simple"
        self._enchantements = []

    def lame(self, materiau):
        if materiau not in LAMES:
            raise ValueError(f"Matériau inconnu : {materiau}")
        self._lame = materiau
        return self

    def garde(self, style):
        self._garde = style
        return self

    def enchanter(self, enchantement):
        if len(self._enchantements) >= MAX_ENCHANTEMENTS:
            raise ValueError("Une lame ne supporte pas plus de 3 enchantements")
        self._enchantements.append(enchantement)
        return self

    def forger(self):
        if self._lame is None:
            raise ValueError("Impossible de forger sans lame")
        degats = LAMES[self._lame] + BONUS_ENCHANTEMENT * len(self._enchantements)
        return Epee(self._lame, self._garde, tuple(self._enchantements), degats)


def epee_du_chevalier():
    return ForgeBuilder().lame("acier").garde("dorée").enchanter("sacré").forger()


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
