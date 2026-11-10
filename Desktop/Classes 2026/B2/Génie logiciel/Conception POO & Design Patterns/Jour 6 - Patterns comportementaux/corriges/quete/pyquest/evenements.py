"""Observer : un bus d'événements.

Le combat PUBLIE ce qui se passe ; le journal, les succès (et demain les sons,
les statistiques, l'interface graphique…) S'ABONNENT. Le combat ne les connaît pas.
"""
from collections import defaultdict


class BusEvenements:
    def __init__(self):
        self._abonnes = defaultdict(list)

    def abonner(self, evenement, callback):
        self._abonnes[evenement].append(callback)

    def desabonner(self, evenement, callback):
        self._abonnes[evenement].remove(callback)

    def publier(self, evenement, **donnees):
        # copie de la liste : un abonné peut se désabonner pendant la notification
        for callback in list(self._abonnes[evenement]):
            callback(**donnees)


class Journal:
    """Observateur : garde une trace lisible de tout ce qui se passe."""

    def __init__(self, bus):
        self.lignes = []
        bus.abonner("action", self.sur_action)
        bus.abonner("attaque", self.sur_attaque)
        bus.abonner("victoire", self.sur_victoire)
        bus.abonner("defaite", self.sur_defaite)
        bus.abonner("succes", self.sur_succes)

    def sur_action(self, message):
        self.lignes.append(message)

    def sur_attaque(self, auteur, cible, degats):
        self.lignes.append(f"{auteur.nom} inflige {degats} dégâts à {cible.nom}")

    def sur_victoire(self, hero, adversaire):
        self.lignes.append(f"{adversaire.nom} est vaincu !")

    def sur_defaite(self, hero, adversaire):
        self.lignes.append(f"{hero.nom} est tombé au combat…")

    def sur_succes(self, nom):
        self.lignes.append(f"*** Succès débloqué : {nom} ***")


class ChasseurDeSucces:
    """Observateur qui publie à son tour un événement « succes »."""

    COUP_DE_MAITRE = 20

    def __init__(self, bus):
        self.bus = bus
        self.victoires = 0
        self.debloques = []
        bus.abonner("victoire", self.sur_victoire)
        bus.abonner("attaque", self.sur_attaque)

    def sur_victoire(self, hero, adversaire):
        self.victoires += 1
        if self.victoires == 1:
            self._debloquer("Premier sang")
        if self.victoires == 3:
            self._debloquer("Chasseur")
        if hasattr(adversaire, "enrage"):          # seuls les boss peuvent enrager
            self._debloquer("Tueur de boss")

    def sur_attaque(self, auteur, cible, degats):
        if degats >= self.COUP_DE_MAITRE:
            self._debloquer("Coup de maître")

    def _debloquer(self, nom):
        if nom not in self.debloques:
            self.debloques.append(nom)
            self.bus.publier("succes", nom=nom)
