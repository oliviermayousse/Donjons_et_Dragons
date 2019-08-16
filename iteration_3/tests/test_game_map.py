from src.game.game_map import Map, NotEmptyException
from src.game.ennemi import Ennemi
from src.game.coffre import Coffre
import pytest


def test_map_get_name():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_name() == "Choco Island"


def test_map_get_number_of_case():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_number_of_case() == 64


def test_get_creat_map():
    game_map = Map(name="Choco Island", number_of_case=64, liste_ennemis=Ennemi.get_list_ennemi(), liste_coffres=Coffre.get_list_coffre())
    assert game_map.get_creat_map()


def test_exception():

        game_map = Map(name="Choco Island", number_of_case=64, liste_ennemis=[Ennemi("Dragon", "\033[32m🐉\033[0m", 2, 15, 4)],
                       liste_coffres=[Coffre("Arc", "\033[34m🏹\033[0m", 2, 0, 1)])

        with pytest.raises(NotEmptyException):
            game_map.get_creat_map()