"""Entraînement 4 · L'armurerie 

1. Écrivez une dataclass Arme(nom, degats, rarete="commune") :
   - immuable (frozen) et ordonnable (order) selon les dégâts, puis le nom ;
   - __post_init__ refuse des dégâts <= 0 et une rareté inconnue
     (RARETES = ("commune", "rare", "épique", "légendaire")).
2. Écrivez une dataclass Armurerie(nom) qui contient une liste d'armes
   (attention au piège de la liste par défaut !) avec :
   - ajouter(arme) ;
   - plus_puissante() -> l'arme aux plus gros dégâts (None si vide) ;
   - par_rarete(rarete) -> la liste des armes de cette rareté, triées.
"""


from dataclasses import dataclass, field

RARETES = ("commune", "rare", "épique", "légendaire")


# TODO : @dataclass(...) Arme
# Indice : l'ordre des champs compte pour order=True


# TODO : @dataclass Armurerie avec ajouter, plus_puissante, par_rarete


if __name__ == "__main__":
    forge = Armurerie("La Forge du Nain")
    for a in [Arme(8, "Épée courte"), Arme(25, "Excalibur", "légendaire"), Arme(12, "Hache", "rare"), Arme(10, "Arc", "rare")]:
        forge.ajouter(a)
    assert forge.plus_puissante().nom == "Excalibur"
    assert [a.nom for a in forge.par_rarete("rare")] == ["Arc", "Hache"]
    assert Armurerie("Vide").plus_puissante() is None
    assert Armurerie("A").armes is not Armurerie("B").armes  # chaque armurerie a SA liste
    try:
        Arme(5, "Bâton", "mythique")
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError attendue")
    print("Tous les tests passent !")
