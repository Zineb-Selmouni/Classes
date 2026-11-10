# Quête 5 · L'équipement, les hordes et le tableau des scores

On repart du corrigé de la quête 4. Cinq nouveaux fichiers, un pattern de structure chacun.

## Lancer

```bash
python -m pytest
python -m pyquest.jeu      # mettez la démo à jour à la fin
```

## Étapes

1. `scores.py` : un **Adapter** pour brancher l'API `ArcadeCloudAPI` du partenaire
   (qu'on n'a pas le droit de modifier) sur notre interface `TableauDesScores`.
2. `enchantements.py` : des **Decorator** pour enchanter les armes (feu, givre, affûtée),
   cumulables à volonté.
3. `groupes.py` : un **Composite** : `GroupeDeMonstres` se combat comme un seul monstre.
   `combat()` ne doit pas être modifié !
4. `catalogue.py` : deux **Proxy** devant le catalogue distant : un cache et une protection.
5. `aventure.py` : une **Facade**, `Aventure`, qui cache tout le moteur derrière 3 méthodes.

## Bonus

- Un enchantement « vampirique » qui soigne le héros à chaque coup : pourquoi est-ce plus
  difficile avec un simple Decorator d'arme ? Quelle solution proposez-vous ?
- Un `ProxyJournal` qui note chaque appel au catalogue.
- Un menu en ligne de commande (input) qui n'utilise QUE la façade `Aventure`.
