# Contrôle · Conception POO & Design Patterns

**B2 · Génie logiciel · Jour 6 · Durée : 1 heure · Noté sur 20**

Nom : ______________________  Prénom : ______________________

> Documents, ordinateurs et téléphones interdits. Répondez directement sur la copie.
> Le code peut être écrit en Python simplifié : on évalue la conception, pas la virgule.

---

## Partie A · QCM (8 points, 1 point par question, une seule bonne réponse)

**A1.** Qu'affiche ce programme ?

```python
class Sac:
    objets = []

    def ajouter(self, objet):
        self.objets.append(objet)

a, b = Sac(), Sac()
a.ajouter("épée")
print(b.objets)
```

☐ A. `[]`  ☐ B. `['épée']`  ☐ C. `AttributeError`  ☐ D. `None`

**A2.** À quoi sert principalement `@property` ?

☐ A. À rendre un attribut privé, inaccessible depuis l'extérieur
☐ B. À accéder à une méthode comme à un attribut, par exemple pour valider ou calculer une valeur
☐ C. À déclarer un attribut de classe partagé par toutes les instances
☐ D. À rendre une méthode abstraite

**A3.** `Forme` hérite de `ABC` et déclare `aire()` avec `@abstractmethod`. Que fait `Forme()` ?

☐ A. Crée un objet dont `aire()` renvoie `None`
☐ B. Lève une `TypeError`
☐ C. Crée un objet, l'erreur n'arrive qu'à l'appel de `aire()`
☐ D. Lève une `NotImplementedError`

**A4.** Une fonction `prix(produit)` contient une cascade de `if isinstance(produit, …)`, et il faut la modifier à chaque nouveau type de produit. Quel principe SOLID est d'abord violé ?

☐ A. S, responsabilité unique  ☐ B. O, ouvert/fermé  ☐ C. I, ségrégation des interfaces  ☐ D. D, inversion des dépendances

**A5.** Quel est le principal reproche fait au Singleton ?

☐ A. Il consomme beaucoup de mémoire
☐ B. Il est impossible à écrire en Python
☐ C. C'est un état global caché, qui complique les tests et couple les classes
☐ D. Il empêche l'héritage

**A6.** Decorator et Proxy ont une structure très proche. Qu'est-ce qui les distingue ?

☐ A. Le Proxy hérite toujours de la classe réelle
☐ B. Le Decorator change l'interface de l'objet
☐ C. Leur intention : ajouter des comportements (Decorator) ou contrôler l'accès (Proxy)
☐ D. Rien, ce sont deux noms pour le même pattern

**A7.** Plusieurs objets doivent être prévenus quand l'état d'un autre change, sans que celui-ci les connaisse. Quel pattern ?

☐ A. Observer  ☐ B. Facade  ☐ C. Command  ☐ D. Builder

**A8.** On veut choisir, pendant l'exécution, l'algorithme de calcul des frais de port (standard, express, gratuit). Quel pattern ?

☐ A. State  ☐ B. Strategy  ☐ C. Template Method  ☐ D. Adapter

---

## Partie B · Reconnaître les patterns (4 points)

Pour chaque extrait, **nommez le pattern** (0,5 pt) et **justifiez en une phrase** (0,5 pt).

**B1.**

```python
class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

Pattern : ______________________ Justification : ________________________________________

**B2.**

```python
class MeteoEnCache:
    def __init__(self, service):
        self._service = service
        self._memoire = {}

    def temperature(self, ville):
        if ville not in self._memoire:
            self._memoire[ville] = self._service.temperature(ville)
        return self._memoire[ville]
```

Pattern : ______________________ Justification : ________________________________________

**B3.**

```python
class Rapport(ABC):
    def generer(self):
        return self.entete() + self.corps() + self.pied()

    def entete(self):
        return "=== Rapport ===\n"

    @abstractmethod
    def corps(self): ...

    def pied(self):
        return "\n=== Fin ==="

class RapportVentes(Rapport):
    def corps(self):
        return "Ventes : 1 200 €"
```

Pattern : ______________________ Justification : ________________________________________

**B4.**

```python
class Bouton:
    def __init__(self, action):
        self.action = action

    def clic(self):
        self.action.executer()
        historique.append(self.action)

def ctrl_z():
    historique.pop().annuler()
```

Pattern : ______________________ Justification : ________________________________________

---

## Partie C · Conception : le lecteur de musique (8 points)

Une application de musique veut un `Lecteur` qui :

- joue une liste de morceaux selon un **mode de lecture** que l'utilisateur peut changer
  **pendant** la lecture : *dans l'ordre*, *aléatoire*, et demain d'autres modes
  (*répéter un morceau*…), **sans modifier** la classe `Lecteur` ;
- **prévient** l'écran, la notification du téléphone et le service de statistiques à chaque
  nouveau morceau. Le `Lecteur` ne doit **pas connaître** ces classes, et on doit pouvoir en
  ajouter d'autres.

**C1.** (1 pt) Quels patterns utilisez-vous ? Un par besoin, avec une phrase de justification.

**C2.** (3 pts) Dessinez le **diagramme de classes UML** : classes, interfaces ou classes abstraites,
attributs et méthodes principaux, relations (héritage ou implémentation, association ou composition)
avec leurs flèches correctes.

**C3.** (3 pts) Écrivez en Python :

- l'interface des modes de lecture et les deux modes *dans l'ordre* et *aléatoire*
  (le hasard doit pouvoir être contrôlé dans les tests) ;
- la classe `Lecteur` avec `abonner(observateur)`, `changer_mode(mode)` et `suivant()`,
  qui passe au morceau suivant **selon le mode** et prévient les abonnés ;
- un observateur `Ecran` qui affiche `"♪ <titre>"`.

**C4.** (1 pt) Citez **deux principes SOLID** respectés par votre conception, et expliquez en une
phrase chacun pourquoi.
