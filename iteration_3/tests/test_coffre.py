from src.game.coffre import Coffre


def test_get_list_coffre():
    list_coffre = Coffre.get_list_coffre()
    assert type(list_coffre) == list
    for coffre in list_coffre:
        assert isinstance(coffre, Coffre)

def test__repr_():
    coffre = Coffre("Arc", "\033[34m🏹\033[0m", 2, 0, 1)

    assert repr(coffre) == coffre.image
