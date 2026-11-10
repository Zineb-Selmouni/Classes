# Bases du développement web — Plan du cours

| | |
|---|---|
| **Classe** | B1 |
| **Unité de formation** | Ymmersion |
| **Volume** | 12 h |
| **Dates** | jeudi 19 nov. 2026, vendredi 20 nov. 2026 (9 h – 16 h) |
| **Support** | [Présentation (117 diapositives)](Bases%20du%20développement%20web%20-%20Présentation%20B1.pptx) · [Exemple - page de Noor](Exemple%20-%20page%20de%20Noor/index.html) |
| **Évaluation** | projet « Escape Web » en binôme, présenté en soutenance (dates à fixer) |

## Objectifs

À la fin des deux journées, l'étudiant·e sait :

- expliquer ce qui se passe entre la saisie d'une URL et l'affichage d'une page ;
- écrire une page HTML structurée et sémantique, avec un formulaire ;
- la mettre en forme avec CSS et Flexbox, et la rendre responsive ;
- ajouter des interactions en JavaScript ;
- publier sa page en ligne avec Git et GitHub Pages ;
- mener un projet web avec méthode et le présenter devant un jury.

**Prérequis :** aucun (le cours « Anatomie des ordinateurs » du 22 oct. pose le vocabulaire de base).

**Fil rouge :** chaque étudiant·e construit sa **page de présentation personnelle**, enrichie à chaque partie, puis mise en ligne en fin de jour 2. La démo en direct utilise la page de **Noor**, une étudiante fictive (code complet dans le dossier « Exemple - page de Noor »).

**Checkpoints :** chaque partie se termine par une diapositive jaune « Pour votre projet » (9 au total). Réunies, elles forment le cahier des charges technique du projet.

## Jour 1 — jeudi 19 novembre : le web, HTML & CSS (diapos 1 à 51)

| Partie | Contenu | Activité | Checkpoint |
|---|---|---|---|
| Accueil | Brise-glace, mission en 4 étapes, page de Noor, règles de travail | Un site adoré, un site détesté → critères de qualité | — |
| 01 · Comment marche le web ? | Internet vs web, histoire, client / serveur, URL, DNS, voyage d'une page (avec HTTP), codes de statut, trio HTML / CSS / JS | Jeu de rôle « une requête HTTP » ; défi DevTools | 1 |
| 02 · Mise en place | VS Code, Live Server, arborescence, raccourcis | Créer le dossier de la page perso | 2 |
| 03 · HTML | Balises, squelette, titres, liens, images, listes et tableaux, sémantique et accessibilité | Chasse aux erreurs ; contenu de la page perso | 3 |
| 04 · Formulaires | `form`, `label`, types d'`input`, `select`, `textarea`, `required` | Formulaire de contact | 4 |
| 05 · CSS | Règle, sélecteurs, cascade, couleurs, polices, unités, modèle de boîte | CSS Diner ; habiller la page (variables CSS) | 5 |
| **Fin du jour 1** | Récapitulatif + travail du soir : finir la page, créer son compte GitHub | | |

## Jour 2 — vendredi 20 novembre : Flexbox, responsive, JavaScript & mise en ligne (diapos 52 à 99)

| Partie | Contenu | Activité | Checkpoint |
|---|---|---|---|
| Échauffement | Quiz éclair, méthode de débogage | Chasse aux bugs en binôme | — |
| 06 · Flexbox | `display` block / inline, axes, `justify-content`, `align-items`, recettes menu et cartes | Flexbox Froggy ; menu et cartes en flex | 6 |
| 07 · Responsive | `viewport`, mobile first et media queries, images fluides, aperçu de Grid, mode appareil | Version mobile de la page perso | 7 |
| 08 · JavaScript | Console, variables, conditions, fonctions, DOM, événements, lecture des erreurs | 3 recettes : mode sombre, message selon l'heure, validation du formulaire | 8 |
| 09 · Mise en ligne | Git en 4 commandes, GitHub Pages, messages de commit | Publier la page | 9 |
| Galerie | 1 min par personne, « deux étoiles et un souhait » | Première mini-soutenance | — |
| **Fin du jour 2** | Ressources, glossaire, ce qu'il faut retenir | | |

## Projet final — « Escape Web » (diapos 100 à 117)

À lancer en fin de jour 2 si le temps le permet, ou lors d'une séance dédiée.

**Le sujet :** en binôme, créer un **escape game jouable dans le navigateur**. Le joueur est « enfermé » dans le site : il traverse une page d'accueil (histoire et règles), 3 salles et une page de sortie. Pour passer d'une salle à la suivante, il doit résoudre une énigme et taper le bon code dans un cadenas (formulaire vérifié en JavaScript). Le thème est libre : laboratoire, musée hanté, vaisseau en panne… Le jour de la soutenance, c'est le jury qui joue.

**Pourquoi ce sujet :** chaque type d'énigme oblige à utiliser une compétence du cours, et les niveaux argent et or poussent les plus à l'aise à apprendre seuls.

### Les énigmes (au moins 3 types différents)

| Énigme | Principe | Compétence |
|---|---|---|
| Le code source | Indice caché dans un commentaire `<!-- -->` | HTML |
| L'inspecteur | Texte invisible (même couleur que le fond, `display: none`) | CSS + DevTools |
| Le binaire | Code écrit en 0 et 1 | Binaire (cours d'octobre) |
| Le survol | Indice visible au `:hover` | CSS |
| Le petit écran | Indice visible seulement sur mobile | Media queries |
| Le cadenas | Formulaire + vérification du code | Formulaire + JavaScript |

### Niveaux de défi

- **Bronze (obligatoire) :** 5 pages (accueil, 3 salles, sortie), 3 types d'énigmes, un cadenas JS par salle, jouable sur téléphone et en ligne.
- **Argent :** chronomètre, compteur d'essais ratés, bouton « indice » qui coûte du temps, animations CSS.
- **Or :** meilleur temps sauvegardé (`localStorage`), inventaire d'objets entre les salles, code impossible à lire dans le JS, énigme inédite.
- Argent et or : jusqu'à +2 points de bonus (note plafonnée à 20).

### Cahier des charges technique (les 9 checkpoints)

- **HTML :** pages reliées par un menu commun (accueil, règles, crédits) ; balises sémantiques ; un `h1` par page ; `alt` sur chaque image ; zéro erreur W3C.
- **Formulaire :** les cadenas ; labels reliés, bons types, `required`.
- **CSS :** feuille externe, aucun style inline ; 3-4 couleurs en variables, 2 polices max ; contrastes ; états `:hover`.
- **Mise en page :** Flexbox ou Grid, jamais de tableaux.
- **Responsive :** `viewport` ; OK à 360, 768 et 1 280 px ; pas de défilement horizontal.
- **JavaScript :** fichier séparé + `defer` ; zéro erreur console.
- **Git & en ligne :** commits réguliers et clairs ; jeu sur GitHub Pages ; README complet.

### Jalons

Lancement (équipe, thème, dépôt) → Jalon 1 (histoire, énigmes, arborescence, wireframes) → Jalon 2 (salles en HTML et CSS) → Jalon 3 (cadenas en JS, responsive, test par un autre binôme) → Rendu → Soutenance.

### Livrables

Le jeu en ligne (GitHub Pages), le dépôt GitHub avec son historique, un README (histoire, solution de chaque énigme pour le jury, sources et crédits), un support de soutenance.

### Soutenance

10 min + 5 min de questions : l'histoire, **le jury joue en direct**, choix de conception, zoom sur le code (le cadenas ou l'énigme dont on est fier), difficultés, bilan.

### Grille d'évaluation (sur 20)

| Critère | Points |
|---|---|
| Scénario, énigmes et jouabilité | 3 |
| HTML sémantique et valide | 3 |
| CSS et charte graphique | 3 |
| Responsive | 3 |
| JavaScript | 2 |
| Git et mise en ligne | 2 |
| Soutenance | 4 |
| Bonus argent / or | jusqu'à +2 |

## Outils et ressources

- VS Code + Live Server, Chrome / Firefox DevTools, Git, GitHub, GitHub Pages
- MDN Web Docs (en français), validateur W3C, CSS Diner, Flexbox Froggy, Grid Garden, Coolors, Google Fonts, Unsplash / Pexels, Can I use

## Points à confirmer

- Dates des jalons, du rendu et de la soutenance (annoncées à l'oral : elles ne figurent pas dans la présentation).
- Politique de l'école sur l'IA générative (diapositive « Les règles du jeu »).
- Les étudiant·e·s ont-ils un compte GitHub ? Sinon, le créer le soir du jour 1.
- Préparer un document partagé (ou un mur Padlet) pour collecter les URL avant la galerie du jour 2.
