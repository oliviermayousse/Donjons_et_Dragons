from ..src.game.enemy import Enemy


def test_get_list_enemies():
    list_enemies = Enemy.get_list_enemies()
    assert type(list_enemies) == list
    for enemy in list_enemies:
        assert isinstance(enemy, Enemy)

def test_life_points():
    value = 10
    enemy = Enemy.get_list_enemies()[0]
    enemy.life_points = value
    assert enemy.life_points == enemy._life_points
    enemy.life_points = -2
    assert enemy.life_points == 0
    assert enemy._life_points == 0

def test_repr():
    enemi = Enemy("Dragon", "🐉", 1, 2, 3)
    assert repr(enemi) == enemi.image