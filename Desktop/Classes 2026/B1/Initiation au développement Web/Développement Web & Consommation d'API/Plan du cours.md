# Développement Web & Consommation d'API — Plan du cours

| | |
|---|---|
| **Classe** | B1 |
| **Unité de formation** | Initiation au développement Web |
| **Volume** | 48 h |
| **Dates** | jeu. 7, ven. 8, jeu. 21, ven. 22, jeu. 28, ven. 29 janv., jeu. 4, ven. 5 févr. 2027 (8 journées de 6 h) |
| **Évaluation** | non planifiée (proposition plus bas) |

## Objectifs

À la fin du module, l'étudiant·e sait :

- construire une interface web responsive en HTML / CSS (Flexbox, Grid) ;
- programmer en JavaScript moderne (ES6+) et manipuler le DOM ;
- comprendre le protocole HTTP, le format JSON et les principes d'une API REST ;
- consommer une API avec `fetch` et `async / await` : lecture, envoi, gestion des erreurs et des temps de chargement ;
- livrer une petite application web en ligne, versionnée avec Git.

**Prérequis :** « Bases du développement web » (immersion, 19–20 nov.).

**Fil rouge :** une **application web qui consomme une API publique** (au choix : Pokédex avec PokeAPI, explorateur de pays avec REST Countries, météo avec Open-Meteo, films avec TMDB). Elle grandit de séance en séance et constitue le projet évalué.

## Déroulé par séance

### Séance 1 — jeudi 7 janvier : remise à niveau & outils
- Rappels HTML sémantique et CSS (modèle de boîte, Flexbox), accessibilité de base
- Git & GitHub en équipe : branches, commits propres, pull requests
- Organisation d'un projet front (dossiers, conventions de nommage)
- **TP :** intégrer une maquette simple fournie (page d'accueil) et la pousser sur GitHub

### Séance 2 — vendredi 8 janvier : CSS avancé & responsive
- CSS Grid, positionnement, variables CSS, transitions
- Responsive mobile first, media queries, unités relatives
- **TP :** maquette multi-sections responsive (cartes, grille, navigation mobile)
- **Fil rouge :** choix de l'API, maquette papier / Figma de l'application

### Séance 3 — jeudi 21 janvier : JavaScript fondamentaux
- Variables (`let` / `const`), types, opérateurs, conditions, boucles
- Fonctions (déclarations, fléchées), portée
- Tableaux et objets, méthodes `map`, `filter`, `find`, `reduce`
- **TP :** exercices progressifs (type kata) puis manipulation d'un jeu de données JSON local

### Séance 4 — vendredi 22 janvier : DOM & événements
- Sélection et création d'éléments, `textContent` vs `innerHTML` (risque XSS)
- Événements, délégation, formulaires et validation
- Stockage local (`localStorage`), modules ES (`import` / `export`)
- **TP :** application de liste de tâches complète (ajout, filtre, persistance)

### Séance 5 — jeudi 28 janvier : HTTP, JSON & premières requêtes
- HTTP en détail : méthodes, codes de statut, en-têtes, corps de requête
- API REST : ressources, endpoints, paramètres de requête, pagination
- Explorer une API avec Bruno ou Postman, lire une documentation d'API
- Asynchrone en JS : promesses, `async / await`, `fetch` (GET)
- **Fil rouge :** afficher la liste des éléments de l'API choisie

### Séance 6 — vendredi 29 janvier : consommer une API proprement
- `fetch` en POST / PUT / DELETE (avec JSONPlaceholder ou une API d'entraînement)
- Gestion des erreurs (`try / catch`, `response.ok`), états de chargement et d'erreur dans l'interface
- Recherche, filtres, pagination côté client, `debounce`
- CORS (comprendre l'erreur), clés d'API : pourquoi on ne les expose pas côté client
- **Fil rouge :** page de détail, recherche et gestion des erreurs

### Séance 7 — jeudi 4 février : projet fil rouge
- Organisation du code (modules, une fonction = une responsabilité)
- Revue de code entre pairs, accessibilité et performance (Lighthouse)
- Déploiement (GitHub Pages / Netlify)
- **Atelier encadré :** développement du projet, points individuels

### Séance 8 — vendredi 5 février : finalisation & évaluation
- Matinée : finitions et préparation de la démo
- Après-midi : soutenances (10 min par personne ou binôme : démo + questions sur le code)
- Bilan du module

## Évaluation (proposition)

| Épreuve | Poids | Modalité |
|---|---|---|
| Projet fil rouge | 60 % | Code sur GitHub + application en ligne + soutenance le 5 févr. |
| TP noté | 40 % | Séance 6 ou 7 : consommer une API inconnue en temps limité (2 h) |

**Grille du projet :** fonctionnement (appels API, erreurs gérées), qualité du code, interface responsive, historique Git, clarté de la soutenance.

## Outils et ressources

- VS Code, DevTools (onglet Network), Bruno ou Postman, GitHub, Netlify
- MDN Web Docs, javascript.info (version française), liste « public-apis » sur GitHub

## Points à confirmer

- Travail individuel ou en binôme pour le projet ?
- Faut-il introduire un framework (React / Vue), ou rester en JavaScript natif ? Le plan reste en JavaScript natif, plus formateur en B1.
