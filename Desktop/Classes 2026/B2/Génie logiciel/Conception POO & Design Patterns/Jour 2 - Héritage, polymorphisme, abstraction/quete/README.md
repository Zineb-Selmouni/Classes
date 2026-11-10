# Quête 2 · PyQuest v0.2 — Les classes de héros

Le dossier `pyquest/` contient le corrigé de la quête 1. Le studio veut maintenant
des guerriers, des mages, des archers et des boss… sans dupliquer le code.

## Lancer

```bash
python -m pytest          # les nouveaux tests de la v0.2
python -m pyquest.jeu     # la démo (à mettre à jour à la fin)
```

## Étapes

1. `personnages.py` : une classe abstraite `Personnage(nom, pv_max)` qui regroupe tout
   le code commun (pv, est_vivant, recevoir_degats, attaquer, __str__, __repr__).
   Méthode abstraite `degats_de_base()`, propriété `chance_critique` (0 par défaut).
2. `Hero(nom, arme=None)` hérite de `Personnage` : PV de départ dans l'attribut de classe
   `PV_DE_DEPART = 100`, niveau, XP, arme, inventaire. Méthode abstraite
   `capacite_speciale(cible, rng)` qui renvoie une phrase.
3. `Guerrier` (130 PV, « Coup puissant » : dégâts x 2), `Mage` (80 PV, mana, « Boule de feu » :
   25 dégâts pour 20 mana, sinon attaque normale), `Archer` (+25 % de critique grâce à `super()`,
   « Double tir »).
4. `Monstre(nom, pv, degats, xp_donnee)` hérite de `Personnage` ; `Boss` hérite de `Monstre`
   et fait +50 % de dégâts sous la moitié de ses PV (propriété `enrage`).
5. `objets.py` : le protocole `Consommable` et `Hero.utiliser(objet, cible=None)`
   (remplace `boire`).
6. `combat.py` : le héros utilise sa capacité spéciale tous les 3 tours (polymorphisme !).
7. Tous les tests au vert, puis mettez `jeu.py` à jour : une équipe de 3 héros contre un boss.

## Bonus

- Une classe `Voleur` qui vole un objet au monstre.
- Un mixin `JournalisableMixin` qui ajoute une méthode `journaliser(message)` à n'importe quelle classe.
- Le diagramme de classes de la v0.2 en Mermaid dans ce README.
