from ..src.game.warrior_api import WarriorsAPI
from ..src.game.hero import Hero
from ..src.game.game_map import Map
from ..src.game.game_state import GameState


def test_api_get_heroes():
    api = WarriorsAPI()
    heroes = api.get_heroes()
    assert type(heroes) == list
    for hero in heroes:
        assert isinstance(hero, Hero)


def test_api_get_maps():
    api = WarriorsAPI()
    game_map = api.get_maps()
    assert type(game_map) == list
    for map in game_map:
        assert isinstance(map, Map)


def test_api_create_game():
    api = WarriorsAPI()
    game_state = api.create_game(player_name="test", hero=api.get_heroes()[0], map=api.get_maps()[0])
    assert isinstance(game_state, GameState)

