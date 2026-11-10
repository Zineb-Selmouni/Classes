# Python Backend & FastAPI — Plan du cours

| | |
|---|---|
| **Classe** | B2 |
| **Unité de formation** | Développement avancé & Mise en production |
| **Volume** | 48 h |
| **Dates** | mar. 15, jeu. 17, ven. 18 déc. 2026 ; lun. 4, mar. 5, mar. 12, lun. 18 janv., mar. 19 janv. (matin) 2027 |
| **Évaluation** | ven. 29 janv. 2027, après-midi |

> **Volume horaire :** 7 journées + 1 matinée font 45 h sur une base de 6 h / 3 h, pour 48 h prévues. Si les journées font 6,5 h ou plus, le compte est bon ; sinon, prévoir des TP en autonomie pour les 3 h restantes.

## Objectifs

À la fin du module, l'étudiant·e sait :

- concevoir et développer une API REST en Python avec FastAPI ;
- valider les données avec Pydantic et documenter l'API automatiquement (OpenAPI / Swagger) ;
- persister les données dans PostgreSQL avec SQLAlchemy (ou SQLModel) et gérer les migrations avec Alembic ;
- sécuriser une API : hachage des mots de passe, OAuth2 / JWT, rôles ;
- tester une API (pytest), la conteneuriser (Docker) et l'automatiser (CI) jusqu'à la mise en production.

**Prérequis :** Python, POO (module « Conception POO & Design Patterns » de nov. – déc.), bases de SQL et de HTTP.

**Fil rouge :** une **API de gestion d'événements** (utilisateurs, événements, inscriptions, rôles organisateur / participant), construite couche par couche et déployée en fin de module.

## Déroulé par séance

### Séance 1 — mardi 15 décembre : Python moderne pour le backend
- Environnements virtuels et dépendances (`venv` / `uv`), structure d'un projet, `ruff`
- Typage (`typing`), dataclasses, introduction à Pydantic
- Rappels HTTP / REST : ressources, méthodes, codes de statut, idempotence
- Asynchrone en Python : `async / await`, quand c'est utile (I/O) et quand ce ne l'est pas
- **TP :** premiers modèles Pydantic du fil rouge, validation de données

### Séance 2 — jeudi 17 décembre : premiers pas avec FastAPI
- Application, routes, paramètres de chemin et de requête, corps de requête
- Modèles d'entrée / de sortie (`response_model`), codes de statut, `HTTPException`
- Documentation automatique (Swagger UI, ReDoc), tags, exemples
- **TP :** CRUD des événements en mémoire

### Séance 3 — vendredi 18 décembre : structurer une vraie application
- `APIRouter`, organisation en couches (routes / services / dépôts)
- Système de dépendances (`Depends`) : injection de dépendances appliquée (lien avec le module POO)
- Configuration avec `pydantic-settings` et variables d'environnement
- Gestion des erreurs globale, middlewares, CORS
- **TP :** refactoriser le CRUD en architecture propre ; travail à finir pendant les vacances (facultatif)

### Séance 4 — lundi 4 janvier : base de données
- PostgreSQL avec Docker (premier contact avec `docker compose`)
- SQLAlchemy 2.0 (ou SQLModel) : modèles, session, CRUD, relations 1-N et N-N
- Migrations avec Alembic
- Pagination, filtres et tri côté API
- **TP :** brancher le fil rouge sur PostgreSQL (utilisateurs, événements, inscriptions)

### Séance 5 — mardi 5 janvier : authentification & sécurité
- Hachage des mots de passe (bcrypt / argon2)
- OAuth2 password flow, JWT (access token, expiration), utilisateur courant via `Depends`
- Autorisations par rôle, protection des routes
- Bonnes pratiques : OWASP API Security Top 10, secrets hors du code, limitation de débit (notions)
- **TP :** inscription, connexion, routes réservées aux organisateurs

### Séance 6 — mardi 12 janvier : tests & qualité
- pytest : fixtures, paramétrage, base de test isolée
- `TestClient` / `httpx.AsyncClient`, surcharge des dépendances (`dependency_overrides`)
- Couverture de code, tests d'authentification
- Tâches de fond (`BackgroundTasks`), introduction aux WebSockets (bonus)
- **TP :** suite de tests du fil rouge (objectif ≥ 70 % de couverture)

### Séance 7 — lundi 18 janvier : mise en production
- Dockerfile optimisé (multi-stage, utilisateur non root), `docker compose` API + base de données
- Serveur de production (Uvicorn / Gunicorn workers), logs structurés, endpoint de santé
- Intégration continue avec GitHub Actions : lint (`ruff`), tests, build de l'image
- Déploiement sur une plateforme (Render, Railway, Fly.io) ou un VPS
- **TP :** pipeline CI vert + API déployée accessible en ligne

### Séance 8 — mardi 19 janvier (matin, 3 h) : finalisation
- Revue de code croisée, checklist de mise en production
- Présentation des modalités et de la grille d'évaluation, questions / réponses

### Évaluation — vendredi 29 janvier (après-midi)
Voir ci-dessous.

## Évaluation (proposition pour le 29 janv. après-midi)

| Épreuve | Poids | Modalité |
|---|---|---|
| Projet fil rouge | 60 % | Dépôt GitHub + API déployée, rendu la veille ; soutenance de 15 min le 29 (démo, lecture de code, questions) |
| TP individuel | 40 % | 2 h : ajouter une fonctionnalité à une API fournie (endpoint + validation + test) |

**Grille du projet :** couverture fonctionnelle, architecture et lisibilité, sécurité, tests, conteneurisation / CI / déploiement, qualité de la soutenance.

## Outils et ressources

- Python 3.12+, FastAPI, Pydantic v2, SQLAlchemy 2.0 / SQLModel, Alembic, pytest, Docker, GitHub Actions
- Documentation officielle de FastAPI (très pédagogique, en partie traduite en français), Bruno ou Postman pour tester l'API

## Points à confirmer

- Horaires des journées (voir l'écart 45 h / 48 h ci-dessus).
- Docker est-il installable sur les machines des étudiant·e·s ? Sinon, prévoir une base hébergée ou SQLite pour le développement.
- Plateforme de déploiement imposée par l'école ?
