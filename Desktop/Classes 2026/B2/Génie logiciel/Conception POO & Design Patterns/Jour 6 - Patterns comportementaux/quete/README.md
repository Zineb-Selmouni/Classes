# Quête 6 · PyQuest v1.0 : un moteur qui réagit

On repart du corrigé de la quête 5. Six patterns comportementaux, un par étape.
À la fin, PyQuest est un vrai petit moteur de jeu : un combat publie des événements,
les monstres ont une personnalité, les héros peuvent être empoisonnés, les actions
du campement s'annulent et les donjons se parcourent salle par salle.

## Lancer

```bash
python -m pytest                 # les tests sont rangés par étape
python -m pytest tests/test_1_observer.py
python -m pyquest.jeu            # la démo (à mettre à jour à l'étape 6)
```

## Étapes

1. **Observer** (`evenements.py`) : `BusEvenements` (abonner, desabonner, publier),
   puis deux observateurs : `Journal` et `ChasseurDeSucces`.
2. **State** (`etats.py`) : `Empoisonne` et `Etourdi`.
   Dans `personnages.py`, chaque `Personnage` commence avec `self.etat = Normal()`.
3. **Strategy** (`strategies.py`) : `Prudente`, `Venimeuse`, `Ecrasante`, `Imprevisible`.
   - `personnages.py` : `Monstre(..., strategie=None)` et `Monstre.agir(cible, rng)`.
   - `groupes.py` : `GroupeDeMonstres.agir` et `self.etat = Normal()`.
   - `fabriques.py` : stratégies du gobelin et du roi, nouvelle recette `"araignée"`.
4. **Template Method** (`rencontres.py`) : la méthode `jouer()`, ses étapes,
   puis `Duel`, `Embuscade` et `Entrainement`.
5. **Command** (`commandes.py`) : `Enchanter`, `BoirePotion` et `Historique`
   (annuler / refaire).
6. **Iterator** (`donjon.py`) : `Donjon` avec `__iter__` (générateur) et `__len__`.
   Puis la façade `Aventure` v1.0 :
   - dans `__init__` : `self.bus`, `self.journal`, `self.succes`, `self.historique`,
     et un abonnement à « victoire » qui ajoute l'XP de l'adversaire au score ;
   - `explorer_donjon(biome, nb_salles=3)` : pour chaque salle, publier
     `"--- Salle 1/3 ---"`, jouer une `Embuscade` (1 chance sur 4) ou un `Duel`,
     s'arrêter en cas de défaite, sinon se reposer (+40 % des PV max, état Normal) ;
     renvoyer les lignes du journal écrites pendant le donjon ;
   - `agir(commande)` et `annuler()` passent par l'historique.

## Bonus

- **Équilibrage** : en difficulté « normal », le mage ne survit jamais au donjon.
  Mesurez-le (simulez 100 parties avec des graines différentes), puis proposez une
  correction **sans modifier `Rencontre`** : nouvelle stratégie, potion de mana au repos…
- Un observateur `Statistiques` (dégâts totaux, nombre de critiques…) branché sur le bus.
- Un état `Enrage` pour le boss, à la place de la propriété `enrage` du jour 2.
- Une commande `MacroCommande` qui regroupe plusieurs commandes (Composite + Command).
