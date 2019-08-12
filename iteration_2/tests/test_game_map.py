from src.game.game_map import Map


def test_map_get_name():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_name() == "Choco Island"


def test_map_get_number_of_case():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_number_of_case() == 64
