# pytest --cov=src/ && coverage html

from src.game.game_state import GameState
from src.game.hero import Hero
from src.game.game_map import Map
from src.game.ennemi import Ennemi
from src.game.coffre import Coffre
from random import randint


def test_lance_de(monkeypatch):

    GameState(player_name="Olivier", hero=Hero("Warrior", '\033[34m💪\033[0m', 5, 10, 5, 10),
              map=Map("Donjon", 64, liste_ennemis=Ennemi("Dragon", "\033[32m🐉\033[0m", 1, 15, 4),
                      liste_coffres=Coffre("Arc", "\033[34m🏹\033[0m", 2, 0, 1)))

    def new_lance_de(self):
        return 1
    monkeypatch.setattr(GameState, "lance_de", new_lance_de)


def test_lance_de_random():
    assert GameState.lance_de(randint(1, 6)) >= 1
    assert GameState.lance_de(randint(1, 6)) <= 6



