# Quête 3 · Le grand nettoyage du moteur

`moteur/legacy.py` contient le moteur historique de PyQuest : une seule classe `Partie`
de 200 lignes qui fait tout (création des héros et des monstres, combat, boutique,
potions, succès, sauvegarde, affichage).

**Mission :** le restructurer en respectant SOLID, **sans changer son comportement**.

## Lancer

```bash
python -m pytest
```

- `tests/test_1_golden_master.py` rejoue une partie complète et compare la sortie
  à `tests/attendu.txt`, ligne par ligne. Il doit **toujours** rester vert.
- `tests/test_2_comportements.py` : à compléter (étape 1).

## Étapes

1. **Le filet de sécurité.** Complétez `test_2_comportements.py` (voir les TODO).
   Tous les tests doivent passer sur l'ancien code.
2. **Créer les nouveaux modules** dans `moteur/`, un par responsabilité :
   `classes.py`, `monstres.py`, `hero.py`, `combat.py`, `boutique.py`, `succes.py`,
   `affichage.py`, `stockage.py`.
3. **Remplacer les if/elif par des données** : un dictionnaire de classes de héros,
   un bestiaire, un catalogue d'articles, une liste de règles de succès.
4. **Injecter les dépendances** : `Partie(nom, classe, *, affichage=None, stockage=None, rng=random)`.
   Créez `AffichageMemoire` et `StockageMemoire` pour les tests.
5. **Basculer** : `moteur/__init__.py` exporte la nouvelle `Partie`
   (`from .partie import Partie`). Les tests 1 et 2 doivent rester verts.
6. **Des tests unitaires** pour les nouvelles classes, sans console ni fichier.

Après chaque petite étape : `python -m pytest`, puis un commit Git.

## Bonus

- Ajoutez une liche au bestiaire et un succès « Tueur de dragon » : combien de
  fichiers avez-vous dû modifier ?
- Corrigez le bug du héros mort qui boit une potion… en commençant par un test qui échoue.
- Mesurez la couverture : `pip install pytest-cov` puis `python -m pytest --cov=moteur`.
