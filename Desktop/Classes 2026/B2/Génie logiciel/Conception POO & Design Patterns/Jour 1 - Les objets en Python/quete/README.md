# Quête 1 · PyQuest v0.1

Le noyau du jeu : un héros, des monstres, des armes, des potions et un inventaire.

## Lancer

```bash
python -m pytest          # les tests (ils échouent tant que la quête n'est pas finie)
python -m pyquest.jeu     # la démo, quand tout est codé
```

## Étapes

1. `objets.py` : la dataclass `Potion` (l'exemple `Arme` est donné).
2. `inventaire.py` : la classe `Inventaire` et ses méthodes spéciales.
3. `personnages.py` : la classe `Hero` (propriétés, attaque, potions, XP).
4. `personnages.py` : la classe `Monstre`.
5. `combat.py` : la fonction `combat`.
6. Faire passer **tous** les tests, puis lancer la démo.

## Bonus

- Un monstre qui laisse tomber un objet (butin) à sa mort.
- Des potions de force qui augmentent les dégâts pendant 3 tours.
- Un `__str__` plus joli pour le héros : `Aria ❤ ███████░░░ 70/100`.
