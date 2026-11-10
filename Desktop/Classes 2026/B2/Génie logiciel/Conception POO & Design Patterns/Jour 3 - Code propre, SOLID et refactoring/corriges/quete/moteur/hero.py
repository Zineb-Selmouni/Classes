"""L'état du héros et ses règles, et seulement ça. (S de SOLID.)"""
from .classes import ClasseDeHero, classe_par_nom

XP_PAR_NIVEAU = 100
BONUS_ATTAQUE_PAR_NIVEAU = 2
BONUS_PV_PAR_NIVEAU = 10
OR_DE_DEPART = 20


class Hero:
    def __init__(self, nom, classe: ClasseDeHero):
        self.nom = nom
        self.classe = classe
        self.pv_max = classe.pv
        self.pv = classe.pv
        self.attaque = classe.attaque
        self.crit = classe.crit
        self.niveau = 1
        self.xp = 0
        self.or_ = OR_DE_DEPART
        self.inventaire = []
        self.monstres_tues = 0
        self.succes = []

    @property
    def est_vivant(self):
        return self.pv > 0

    def degats(self):
        return self.attaque + (self.niveau - 1) * BONUS_ATTAQUE_PAR_NIVEAU

    def subir(self, degats_bruts):
        """Applique l'armure, retire les PV et renvoie les dégâts réellement subis."""
        degats = max(0, degats_bruts - self.classe.armure)
        self.pv = max(0, self.pv - degats)
        return degats

    def soigner(self, soin):
        avant = self.pv
        self.pv = min(self.pv_max, self.pv + soin)
        return self.pv - avant

    def recompenser(self, monstre):
        """Donne XP et or. Renvoie la liste des niveaux gagnés."""
        self.xp += monstre.xp
        self.or_ += monstre.or_
        self.monstres_tues += 1
        niveaux = []
        while self.xp >= self.niveau * XP_PAR_NIVEAU:
            self.niveau += 1
            self.pv_max += BONUS_PV_PAR_NIVEAU
            self.pv = self.pv_max
            niveaux.append(self.niveau)
        return niveaux

    # ---- sérialisation
    def vers_dict(self):
        return {"nom": self.nom, "classe": self.classe.nom, "pv": self.pv, "pv_max": self.pv_max,
                "attaque": self.attaque, "crit": self.crit, "niveau": self.niveau, "xp": self.xp,
                "or": self.or_, "inventaire": self.inventaire, "monstres_tues": self.monstres_tues,
                "succes": self.succes}

    @classmethod
    def depuis_dict(cls, data):
        hero = cls(data["nom"], classe_par_nom(data["classe"]))
        hero.pv, hero.pv_max = data["pv"], data["pv_max"]
        hero.attaque, hero.crit = data["attaque"], data["crit"]
        hero.niveau, hero.xp, hero.or_ = data["niveau"], data["xp"], data["or"]
        hero.inventaire = list(data["inventaire"])
        hero.monstres_tues = data["monstres_tues"]
        hero.succes = list(data["succes"])
        return hero

    def resume(self):
        return (f"{self.nom} ({self.classe.nom}) niv. {self.niveau} | PV {self.pv}/{self.pv_max}"
                f" | XP {self.xp} | Or {self.or_} | Sac : " + ", ".join(self.inventaire))
