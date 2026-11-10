# Quête 4 · Les fabriques du donjon

On repart de PyQuest v0.2 (le dossier `pyquest/` contient le corrigé de la quête 2).
Le studio veut des monstres adaptés au niveau et à la difficulté, des biomes,
des salles, une création de héros simple et des variantes de monstres.

## Lancer

```bash
python -m pytest
python -m pyquest.jeu      # quand tout est fini (mettez la démo à jour !)
```

## Étapes

1. `config.py` : la `Configuration` est un **Singleton** (difficulté de la partie).
2. `fabriques.py` : une **fabrique simple** `creer_monstre(type, niveau)` alimentée par
   un registre et le décorateur `@enregistrer`.
3. `fabriques.py` : une **Abstract Factory** `FabriqueDeBiome` (forêt, volcan) qui crée
   un monstre, un trésor et une description cohérents.
4. `salles.py` : une **Factory Method** : chaque `Salle` décide quel monstre elle crée.
5. `construction.py` : un **Builder** de héros, plus le directeur `hero_de_depart`.
6. `prototypes.py` : un registre de **prototypes** qui clone (en profondeur) des monstres.

## Bonus

- Un biome « marais » ajouté sans modifier `generer_rencontre`.
- Remplacez le Singleton par une injection : `creer_monstre(type, niveau, config)`.
  Quels tests deviennent plus simples ?
- Dessinez le diagramme de séquence de `SalleDuTrone(2).entrer(hero)`.
