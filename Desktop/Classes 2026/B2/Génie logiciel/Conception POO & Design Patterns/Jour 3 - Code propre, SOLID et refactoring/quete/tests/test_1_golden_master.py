"""Le filet de sécurité : une partie complète doit produire EXACTEMENT la même sortie
avant et après le refactoring (technique du « golden master »)."""
from pathlib import Path

from moteur import Partie
from tests.scenario import jouer_scenario

ATTENDU = Path(__file__).with_name("attendu.txt")


def test_la_sortie_ne_change_pas(capsys, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    jouer_scenario(Partie)
    sortie = capsys.readouterr().out
    attendu = ATTENDU.read_text(encoding="utf-8")
    assert sortie.splitlines() == attendu.splitlines()
