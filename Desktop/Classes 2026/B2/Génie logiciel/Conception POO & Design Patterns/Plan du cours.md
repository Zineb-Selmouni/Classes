# Conception POO & Design Patterns — Plan du cours

| | |
|---|---|
| **Classe** | B2 |
| **Unité de formation** | Génie logiciel |
| **Volume** | 30 h prévues · 6 journées préparées (9 h – 16 h) |
| **Dates** | lun. 16 nov., mar. 17, jeu. 26, ven. 27 nov., jeu. 3, ven. 4 déc. 2026 |
| **Langage** | Python 3.12+ (pytest) |
| **Évaluation** | projet en binôme 60 % · contrôle écrit d'1 h (jour 6) 40 % |

> **À confirmer :** le calendrier indique le 16 novembre en après-midi seulement. Les 6 jours ont été préparés comme des journées complètes ; si le 16 reste une demi-journée, voir « Si le jour 1 est une demi-journée » plus bas.

## Objectifs

À la fin du module, l'étudiant·e sait :

- modéliser un problème en objets et le représenter en UML (diagrammes de classes et de séquence) ;
- appliquer l'encapsulation, l'héritage, le polymorphisme, l'abstraction, et préférer la composition quand c'est pertinent ;
- reconnaître les défauts de conception (code smells) et les corriger avec les principes SOLID ;
- identifier, expliquer et implémenter 18 design patterns (création, structure, comportement) ;
- justifier un choix de conception, à l'écrit comme à l'oral.

## Fil rouge : PyQuest

Un jeu de rôle textuel en Python qui grandit chaque jour. Chaque nouvelle demande du « studio » casse la conception précédente et justifie un principe ou un pattern.

| Version | Jour | Ce qui arrive |
|---|---|---|
| v0.1 | 1 | Objets, héros, monstres, inventaire, combat (avec du code dupliqué volontairement) |
| v0.2 | 2 | Hiérarchie Personnage / Hero / Guerrier, Mage, Archer / Monstre, Boss ; consommables (Protocol) |
| v0.3 | 3 | Refactoring d'une classe dieu (`legacy.py`) sous filet de tests (golden master) |
| v0.4 | 4 | Configuration (Singleton), fabriques, biomes, salles, HeroBuilder, prototypes |
| v0.5 | 5 | Scores en ligne (Adapter), enchantements (Decorator), hordes (Composite), bestiaire (Proxy), Aventure (Facade) |
| v1.0 | 6 | Bus d'événements et succès (Observer), états, IA des monstres, rencontres, commandes annulables, donjons |

## Déroulé type d'une journée

Cours, puis entraînements (exercices notés de ★ à ★★★), puis **Quête** (le TP PyQuest, avec tests par étape), puis **Boss de fin** (quiz de 6 à 8 questions). Chaque dossier « Jour N » contient :

- `Jour N - ….pptx` : le diaporama, notes de l'enseignant et horaires indicatifs dans les commentaires ;
- `exercices/` : les énoncés (squelettes à compléter, tests en bas de fichier) ;
- `quete/` : le point de départ de la quête, son README et ses tests (`python -m pytest`) ;
- `corriges/` : les corrigés des exercices et de la quête (tous les tests passent).

## Déroulé par journée

### Jour 1 — lundi 16 novembre : les objets en Python
- Classe, objet, `__init__`, attributs d'instance et de classe, méthodes, encapsulation, `@property`
- Méthodes spéciales (`__str__`, `__repr__`, `__eq__`, `__len__`, `__iter__`…), dataclasses
- Diagramme de classes UML
- **Quête 1 :** PyQuest v0.1

### Jour 2 — mardi 17 novembre : héritage, polymorphisme, abstraction
- Héritage, `super()`, redéfinition, polymorphisme
- Classes abstraites (`abc`), protocoles (`typing.Protocol`)
- Composition plutôt qu'héritage (l'explosion combinatoire), associations et agrégations en UML
- **Quête 2 :** PyQuest v0.2

### Jour 3 — jeudi 26 novembre : code propre, SOLID et refactoring
- Code smells, les 5 principes SOLID (avant / après), DRY, KISS, YAGNI, loi de Déméter
- Injection de dépendances, tests de caractérisation, golden master
- **Quête 3 :** refactoriser `legacy.py` sans rien casser

### Jour 4 — vendredi 27 novembre : patterns de création · lancement du projet
- Fabrique simple et registre, Factory Method, Abstract Factory, Builder, Prototype, Singleton (et ses dangers)
- Diagrammes de séquence UML
- **Quête 4 :** PyQuest v0.4 · **Lancement du projet**

### Jour 5 — jeudi 3 décembre : patterns structurels
- Adapter, Decorator (et les décorateurs `@` de Python), Composite, Proxy, Facade, aperçu de Bridge
- **Quête 5 :** PyQuest v0.5 · fin de journée sur le projet

### Jour 6 — vendredi 4 décembre : patterns comportementaux · contrôle
- Strategy, Observer, Command, State, Template Method, Iterator, Chain of Responsibility
- Les patterns dans les frameworks (FastAPI, Django, stdlib) ; synthèse des 18 patterns
- **Quête 6 :** PyQuest v1.0, pendant les **points d'étape projet** (10 min par binôme)
- **Contrôle** de 15 h à 16 h

## Évaluation

| Épreuve | Poids | Modalité |
|---|---|---|
| Projet : votre jeu | 60 % | En binôme, un jeu en Python avec au moins 4 patterns (les 3 familles), UML, SOLID, tests ; rendu le **vendredi 11 décembre** sur GitHub. Sujet et grille : dossier `Projet/`. |
| Contrôle écrit | 40 % | 1 h, fin du jour 6 : QCM (8 pts), reconnaître des patterns (4 pts), conception d'un cas concret (8 pts). Sujet et corrigé : dossier `Contrôle/`. |

## Si le jour 1 est une demi-journée

Garder le cours sur les classes, `@property` et l'UML, et les entraînements 1 à 3 ; donner la quête 1 à terminer en autonomie avant le jour 2, et commencer le jour 2 par sa correction rapide (20 min).

## Outils et ressources

- Python 3.12+, VS Code ou PyCharm, pytest
- UML : Mermaid (dans les README), PlantUML ou draw.io
- refactoring.guru/fr ; *Head First Design Patterns* ; *Game Programming Patterns* (R. Nystrom, gratuit en ligne) ; python-patterns.guide
- Icônes des diaporamas : game-icons.net, licence CC BY 3.0
