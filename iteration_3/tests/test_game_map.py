from ..src.game.game_map import Map, NotEmptyException
from ..src.game.enemy import Enemy
from ..src.game.caissesurprise import CaisseSurprise
import pytest

def test_map_get_name():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_name() == "Choco Island"


def test_map_get_number_of_case():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_number_of_case() == 64


def test_create_map():
    game_map = Map(name="Choco Island", number_of_case=64)
    plateau_de_jeu = game_map.create_map()
    assert type(plateau_de_jeu) == list


def test_NotEmptyException():
    map = Map(name="map test",
              number_of_case=1,
              list_enemies=[Enemy("Dragons", "\033[34m🐉\033[0m", case_enemy=0, attack_level=4, life_points=15)],
              list_caisses_surprises=[CaisseSurprise("Arc", "\033[32m🏹\033[0m", 0, ajout_pt_attack=1, ajout_pt_vie=0)])
    with pytest.raises(NotEmptyException):
        map.create_map()



