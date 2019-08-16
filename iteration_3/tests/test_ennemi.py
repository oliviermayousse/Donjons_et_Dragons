from src.game.ennemi import Ennemi


def test_get_list_ennemi():
    list_ennemi = Ennemi.get_list_ennemi()
    assert type(list_ennemi) == list
    for ennemi in list_ennemi:
        assert isinstance(ennemi, Ennemi)

def test__repr_():
    ennemi = Ennemi("Dragon", "🐉", 45, 15, 4)

    assert repr(ennemi) == ennemi.image


