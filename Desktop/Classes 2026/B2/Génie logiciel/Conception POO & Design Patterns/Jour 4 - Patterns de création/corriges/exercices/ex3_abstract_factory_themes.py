"""Entraînement 3 · Abstract Factory : les thèmes du menu du jeu (corrigé)

Le menu du jeu affiche des boutons et des cadres. En thème clair, tout doit
être clair ; en thème sombre, tout doit être sombre : jamais de mélange.
1. Une fabrique abstraite FabriqueTheme avec creer_bouton(texte) et creer_cadre(titre).
2. ThemeClair : Bouton -> "[ texte ]", Cadre -> "+-- titre --+"
   ThemeSombre : Bouton -> "▐ texte ▌", Cadre -> "█▀▀ titre ▀▀█"
3. La fonction dessiner_menu(fabrique) renvoie les lignes du menu (un cadre « Menu »
   puis les boutons « Jouer » et « Quitter ») sans jamais tester le thème.
4. Ajoutez un ThemeRetro ("<texte>" et "== titre ==") sans modifier dessiner_menu.
"""
from abc import ABC, abstractmethod


class FabriqueTheme(ABC):
    @abstractmethod
    def creer_bouton(self, texte) -> str: ...

    @abstractmethod
    def creer_cadre(self, titre) -> str: ...


class ThemeClair(FabriqueTheme):
    def creer_bouton(self, texte):
        return f"[ {texte} ]"

    def creer_cadre(self, titre):
        return f"+-- {titre} --+"


class ThemeSombre(FabriqueTheme):
    def creer_bouton(self, texte):
        return f"▐ {texte} ▌"

    def creer_cadre(self, titre):
        return f"█▀▀ {titre} ▀▀█"


class ThemeRetro(FabriqueTheme):
    def creer_bouton(self, texte):
        return f"<{texte}>"

    def creer_cadre(self, titre):
        return f"== {titre} =="


def dessiner_menu(fabrique: FabriqueTheme):
    return [fabrique.creer_cadre("Menu"), fabrique.creer_bouton("Jouer"), fabrique.creer_bouton("Quitter")]


if __name__ == "__main__":
    assert dessiner_menu(ThemeClair()) == ["+-- Menu --+", "[ Jouer ]", "[ Quitter ]"]
    assert dessiner_menu(ThemeSombre()) == ["█▀▀ Menu ▀▀█", "▐ Jouer ▌", "▐ Quitter ▌"]
    assert dessiner_menu(ThemeRetro()) == ["== Menu ==", "<Jouer>", "<Quitter>"]
    print("Tous les tests passent !")
