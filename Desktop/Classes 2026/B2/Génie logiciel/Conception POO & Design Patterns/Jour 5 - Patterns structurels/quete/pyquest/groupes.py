"""Étape 3 — Composite : un groupe de monstres se combat comme un seul monstre.

GroupeDeMonstres(nom, membres=()) : ajouter(membre), membres (copie de la liste),
est_vivant (au moins un membre vivant), pv et xp_donnee (sommes),
recevoir_degats(d) (frappe le premier membre vivant), attaquer(cible, rng)
(chaque vivant attaque, renvoie le total), len() (compte les monstres, groupes
imbriqués compris), str() -> "Bande (1/2 debout)".
La fonction combat() doit fonctionner avec un groupe SANS être modifiée.
"""
import random

# TODO
