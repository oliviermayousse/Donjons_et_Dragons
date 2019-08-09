from src.game.warrior_api import WarriorsAPI
from src.game.hero import Hero


def test_api_get_heroes():
    api = WarriorsAPI()
    heroes = api.get_heroes()
    assert type(heroes) == list
    for hero in heroes:
        assert isinstance(hero, Hero)
