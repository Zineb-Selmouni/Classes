"""Entraînement 2 · Observer : le crieur public 

Le crieur de la ville annonce les nouvelles. Il ne connaît pas ses auditeurs :
ils s'abonnent et se désabonnent quand ils veulent.
1. Crieur : abonner(auditeur), desabonner(auditeur), annoncer(nouvelle)
   qui appelle auditeur.notifier(nouvelle) pour chaque abonné.
2. Aventurier(nom, interets) : ne retient (dans self.recues) que les nouvelles
   qui contiennent l'un de ses mots-clés.
3. Garde : retient toutes les nouvelles, préfixées par "[Garde] ".
4. Un auditeur doit pouvoir se désabonner PENDANT une annonce
   (Messager : se désabonne après la 1re nouvelle reçue).
"""


class Crieur:
    # TODO : abonner, desabonner, annoncer
    pass


class Aventurier:
    # TODO : __init__(nom, interets), notifier(nouvelle), attribut recues
    pass


class Garde:
    # TODO
    pass


class Messager:
    """Se désabonne du crieur après la première nouvelle reçue."""

    def __init__(self, crieur):
        self.crieur = crieur
        self.recues = []

    # TODO : notifier


if __name__ == "__main__":
    crieur = Crieur()
    aria, garde = Aventurier("Aria", ["dragon", "trésor"]), Garde()
    messager = Messager(crieur)
    for auditeur in (aria, garde, messager):
        crieur.abonner(auditeur)
    crieur.annoncer("Un dragon survole la ville !")
    crieur.annoncer("Le marché ouvre à midi")
    crieur.desabonner(garde)
    crieur.annoncer("Un trésor a été trouvé")
    assert aria.recues == ["Un dragon survole la ville !", "Un trésor a été trouvé"]
    assert garde.recues == ["[Garde] Un dragon survole la ville !", "[Garde] Le marché ouvre à midi"]
    assert messager.recues == ["Un dragon survole la ville !"]
    print("Tous les tests passent !")
