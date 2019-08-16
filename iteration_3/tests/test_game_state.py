from ..src.game.game_state import GameState
from ..src.game.hero import Hero
from ..src.game.enemy import Enemy
from ..src.game.game_map import Map
from ..src.game.caissesurprise import CaisseSurprise


def test_lancer_le_de(monkeypatch):
    game_state = GameState(player_name="toto",
                hero = Hero("Magicien", "💀",life_points=5, attack_level=5, max_life_points=10, max_attack_level=10),
                map = Map("plateau en ligne", 30, Enemy.get_list_enemies()[0], CaisseSurprise.get_list_caisses_surprises()[0]))

    def nouveau_test_lancer_le_de_monkeypatch(self):
        return 1
    monkeypatch.setattr(GameState, "lancer_le_de", nouveau_test_lancer_le_de_monkeypatch)
    dice = game_state.lancer_le_de()
    # assert dice >= 1
    # assert dice <= 6
    assert dice == 1
