from src.game.game_map import Map
from src.game.objet import Objet
from src.game.ennemie import Ennemie
from src.game.game_status import *
from src.game.hero import Hero
from src.game.game_state import GameState
from src.client.console import ConsoleUI



def test_map_get_name():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_name() == "Choco Island"


def test_map_get_number_of_case():
    game_map = Map(name="Choco Island", number_of_case=64)
    assert game_map.get_number_of_case() == 64


def test_get_map_list():
    list_map = Map.get_carte()
    assert len(list_map) == 2
    assert type(list_map) == list
    for carte in list_map:
        assert isinstance(carte, Map)


def test_get_objet_list():
    list_objet = Objet.get_objet_list()
    assert type(list_objet) == list
    for objet in list_objet:
        assert isinstance(objet, Objet)


def test_get_list_ennemie():
    list_ennemie = Ennemie.get_list_ennemie()
    assert type(list_ennemie) == list
    for ennemie in list_ennemie:
        assert isinstance(ennemie, Ennemie)


def test_get_list_hero():
    list_hero = Hero.get_heroes()
    assert type(list_hero) == list
    for hero in list_hero:
        assert isinstance(hero, Hero)


def test_lancer_de(monkeypatch):
    partie = GameState(player_name="Fabrice", hero=Hero(name="Guerrier", image="🤺", current_life_points=5, max_life_points=10, attaque=5, max_attaque=10), map=Map(name="Forêt", number_of_case=64, ennemies=Ennemie.get_list_ennemie(), objet=Objet.get_objet_list()))

    def lancer_un(self):
        return 1
    monkeypatch.setattr(GameState, "lancer_de_de", lancer_un)
    partie.next_turn()
    assert partie.current_case == 1


def test_calcul_stat():
    partie = GameState(player_name="Fabrice", hero=Hero(name="Guerrier", image="🤺", current_life_points=5, max_life_points=10, attaque=5, max_attaque=10), map=Map(name="Forêt", number_of_case=64, ennemies=Ennemie.get_list_ennemie(), objet=Objet.get_objet_list()))
