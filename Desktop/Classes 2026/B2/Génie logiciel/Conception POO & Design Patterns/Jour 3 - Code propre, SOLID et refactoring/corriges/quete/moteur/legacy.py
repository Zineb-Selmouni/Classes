"""Moteur de PyQuest, écrit en 2019 par un stagiaire pressé.

Ça marche… mais personne n'ose plus y toucher. Le studio veut ajouter
des monstres, des classes, des objets, une sauvegarde en ligne…
Mission : nettoyer ce code SANS changer son comportement.
"""
import json
import random


class Partie:
    def __init__(self, nom, classe):
        self.nom = nom
        self.classe = classe
        if classe == "guerrier":
            self.pv = 130
            self.pv_max = 130
            self.attaque = 9
            self.crit = 0.1
        elif classe == "mage":
            self.pv = 80
            self.pv_max = 80
            self.attaque = 12
            self.crit = 0.05
        elif classe == "archer":
            self.pv = 100
            self.pv_max = 100
            self.attaque = 8
            self.crit = 0.3
        else:
            raise ValueError("classe inconnue : " + classe)
        self.niveau = 1
        self.xp = 0
        self.or_ = 20
        self.inventaire = []
        self.monstres_tues = 0
        self.succes = []

    def creer_monstre(self, type_monstre):
        if type_monstre == "slime":
            return {"nom": "Slime", "pv": 20, "attaque": 3, "xp": 10, "or": 5}
        elif type_monstre == "gobelin":
            return {"nom": "Gobelin", "pv": 35, "attaque": 6, "xp": 25, "or": 12}
        elif type_monstre == "orc":
            return {"nom": "Orc", "pv": 60, "attaque": 10, "xp": 50, "or": 30}
        elif type_monstre == "dragon":
            return {"nom": "Dragon", "pv": 200, "attaque": 25, "xp": 500, "or": 300}
        else:
            raise ValueError("monstre inconnu : " + type_monstre)

    def combattre(self, type_monstre):
        m = self.creer_monstre(type_monstre)
        print("=== Combat : " + self.nom + " contre " + m["nom"] + " ===")
        tour = 1
        while self.pv > 0 and m["pv"] > 0:
            # attaque du héros
            degats = self.attaque + (self.niveau - 1) * 2
            if random.random() < self.crit:
                degats = degats * 2
                print("Tour " + str(tour) + " : COUP CRITIQUE ! " + str(degats) + " dégâts")
            else:
                print("Tour " + str(tour) + " : " + self.nom + " inflige " + str(degats) + " dégâts")
            m["pv"] = m["pv"] - degats
            if m["pv"] <= 0:
                break
            # attaque du monstre
            degats_m = m["attaque"]
            if self.classe == "guerrier":
                degats_m = degats_m - 2  # armure du guerrier
                if degats_m < 0:
                    degats_m = 0
            self.pv = self.pv - degats_m
            if self.pv < 0:
                self.pv = 0
            print("Tour " + str(tour) + " : " + m["nom"] + " inflige " + str(degats_m) + " dégâts")
            tour = tour + 1
        if self.pv > 0:
            print(m["nom"] + " est vaincu !")
            self.xp = self.xp + m["xp"]
            self.or_ = self.or_ + m["or"]
            self.monstres_tues = self.monstres_tues + 1
            while self.xp >= self.niveau * 100:
                self.niveau = self.niveau + 1
                self.pv_max = self.pv_max + 10
                self.pv = self.pv_max
                print(self.nom + " passe au niveau " + str(self.niveau) + " !")
            self.verifier_succes()
            return True
        else:
            print(self.nom + " est mort...")
            return False

    def acheter(self, objet):
        if objet == "potion":
            prix = 10
        elif objet == "grande potion":
            prix = 25
        elif objet == "epee":
            prix = 50
        else:
            print("Objet inconnu")
            return False
        if self.classe == "archer":
            prix = prix - 2  # réduction de la guilde des archers
        if self.or_ < prix:
            print("Pas assez d'or !")
            return False
        self.or_ = self.or_ - prix
        self.inventaire.append(objet)
        if objet == "epee":
            self.attaque = self.attaque + 5
        print(self.nom + " achète : " + objet + " (" + str(prix) + " pièces)")
        return True

    def boire(self):
        if "grande potion" in self.inventaire:
            self.inventaire.remove("grande potion")
            soin = 50
        elif "potion" in self.inventaire:
            self.inventaire.remove("potion")
            soin = 20
        else:
            print("Aucune potion !")
            return 0
        avant = self.pv
        self.pv = self.pv + soin
        if self.pv > self.pv_max:
            self.pv = self.pv_max
        print(self.nom + " boit une potion : +" + str(self.pv - avant) + " PV")
        return self.pv - avant

    def verifier_succes(self):
        if self.monstres_tues >= 1 and "Premier sang" not in self.succes:
            self.succes.append("Premier sang")
            print("Succès débloqué : Premier sang")
        if self.monstres_tues >= 5 and "Chasseur" not in self.succes:
            self.succes.append("Chasseur")
            print("Succès débloqué : Chasseur")
        if self.or_ >= 100 and "Riche" not in self.succes:
            self.succes.append("Riche")
            print("Succès débloqué : Riche")
        if self.niveau >= 3 and "Vétéran" not in self.succes:
            self.succes.append("Vétéran")
            print("Succès débloqué : Vétéran")

    def sauvegarder(self):
        data = {"nom": self.nom, "classe": self.classe, "pv": self.pv, "pv_max": self.pv_max,
                "attaque": self.attaque, "crit": self.crit, "niveau": self.niveau, "xp": self.xp,
                "or": self.or_, "inventaire": self.inventaire, "monstres_tues": self.monstres_tues,
                "succes": self.succes}
        f = open("sauvegarde.json", "w", encoding="utf-8")
        f.write(json.dumps(data))
        f.close()
        print("Partie sauvegardée")

    def charger(self):
        f = open("sauvegarde.json", encoding="utf-8")
        data = json.loads(f.read())
        f.close()
        self.nom = data["nom"]
        self.classe = data["classe"]
        self.pv = data["pv"]
        self.pv_max = data["pv_max"]
        self.attaque = data["attaque"]
        self.crit = data["crit"]
        self.niveau = data["niveau"]
        self.xp = data["xp"]
        self.or_ = data["or"]
        self.inventaire = data["inventaire"]
        self.monstres_tues = data["monstres_tues"]
        self.succes = data["succes"]
        print("Partie chargée")

    def afficher(self):
        print(self.nom + " (" + self.classe + ") niv. " + str(self.niveau) + " | PV " + str(self.pv) + "/"
              + str(self.pv_max) + " | XP " + str(self.xp) + " | Or " + str(self.or_)
              + " | Sac : " + ", ".join(self.inventaire))
