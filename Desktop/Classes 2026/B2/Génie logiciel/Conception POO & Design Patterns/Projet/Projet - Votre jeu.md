# Projet · Concevez votre jeu

**Module :** Conception POO & Design Patterns (B2) · **En binôme** · **60 % de la note du module**

## Le sujet

Concevez et programmez un petit jeu en Python. Il peut se jouer dans le terminal
(conseillé) ou utiliser une bibliothèque graphique (pygame, arcade).

**Le jeu est un prétexte : c'est la qualité de la conception qui est évaluée.**
Un petit jeu très bien conçu vaut mieux qu'un grand jeu en désordre.

## Exigences

1. **Au moins 4 design patterns**, dont au moins un de chaque famille :
   création, structure et comportement. Chaque pattern doit répondre à un vrai
   problème de votre jeu, et ce choix doit être justifié dans le rapport.
2. **Un diagramme de classes UML** (en Mermaid, dans le README) et **au moins un
   diagramme de séquence** pour une interaction importante du jeu.
3. **Un code propre** : principes SOLID, pas de classe « dieu », pas de chaînes de
   `if/elif` sur des types, dépendances injectées (hasard, affichage, sauvegarde…).
4. **Des tests pytest** sur la logique du jeu (pas sur l'affichage), qui passent tous.
5. **Un dépôt GitHub** avec des commits réguliers des deux membres du binôme.

## Idées de jeux

| Jeu | Patterns qui s'y prêtent bien |
|---|---|
| Roguelike textuel (donjon, salles, objets, monstres) | Factory, Strategy (IA), State (effets), Command (actions) |
| Jeu de cartes (deck-builder, bataille) | Decorator (cartes améliorées), Command, Observer, Prototype |
| Tower defense sur une grille | Factory, Strategy (ciblage), Observer, Composite (vagues) |
| Gestion de taverne (clients, commandes, stock) | Builder, State, Observer, Facade |
| Jeu de plateau (dames, puissance 4) avec annulation | Command (annuler / refaire), State, Strategy (IA) |
| Votre idée | à valider avec l'enseignant·e |

## Calendrier (proposition)

| Quand | Étape |
|---|---|
| Jour 4 (ven. 27 nov.) | Binôme formé, idée validée, dépôt GitHub créé avec un README |
| Jour 5 (jeu. 3 déc.) | Diagramme de classes v1, premiers patterns en place |
| Jour 6 (ven. 4 déc.) | Jeu jouable ; point d'étape de 10 minutes avec l'enseignant·e |
| Ven. 11 déc. | **Rendu final** : lien du dépôt GitHub (README + rapport + code + tests) |

## Livrables

- **Le code** du jeu et ses tests, dans le dépôt GitHub.
- **Le README** : présentation du jeu, comment l'installer et y jouer, comment lancer
  les tests, le diagramme de classes et le diagramme de séquence (Mermaid).
- **Le rapport** (3 à 5 pages, PDF ou Markdown dans le dépôt). Pour chaque pattern :
  - le problème rencontré dans votre jeu ;
  - pourquoi ce pattern plutôt qu'une autre solution ;
  - où il se trouve dans le code (fichiers, classes) ;
  - ce qu'il vous a apporté et ce qu'il vous a coûté.

## Grille d'évaluation (sur 20)

| Critère | Points |
|---|---|
| Patterns pertinents, bien implémentés et justifiés | 6 |
| Qualité du code (SOLID, lisibilité, nommage, pas de duplication) | 4 |
| Diagrammes UML (classes et séquence), cohérents avec le code | 3 |
| Tests (pertinence, couverture de la logique du jeu) | 3 |
| Rapport et README | 2 |
| Le jeu fonctionne et est jouable | 2 |

Un pattern présent mais non justifié (ou plaqué sans raison) ne rapporte aucun point.

## Règles

- **IA et tutoriels :** autorisés pour apprendre et vous débloquer. Vous devez pouvoir
  expliquer chaque ligne de votre code (le point d'étape du jour 6 le vérifie).
  Indiquez dans le rapport les outils utilisés et pour quoi.
- **Travail en binôme :** les deux membres doivent avoir des commits. En cas de
  déséquilibre important, la note peut être individualisée.
- **Retard :** un rendu en retard perd 2 points par jour.
- **Plagiat :** le code copié d'un autre binôme vaut 0 aux deux binômes.
