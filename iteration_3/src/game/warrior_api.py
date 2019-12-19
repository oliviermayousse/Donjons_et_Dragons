from .hero import Hero
from .game_map import Map
from .game_state import GameState
from .ennemi import Ennemi
from .coffre import Coffre
# from ..client.console import ConsoleUI


class WarriorsAPI(object):
    """the Warriors Game API"""

    def get_heroes(self):
        """
        Called by the client to retrieve the list of available heroes.

        Returns
            list: the list of available heroes

        """

        return Hero.list_hero()

    def get_maps(self):
        """
        Called by the client to retrieve the list of available maps.

        Returns
            list: the list of available maps
        """

        list_maps = [Map("Donjon", 64, Ennemi.get_list_ennemi(), Coffre.get_list_coffre())]

        return list_maps

    def create_game(self, player_name, hero, map, debug):
        """Called by the client to create a new game

        Args:
            player_name (str): the name of the player
            hero (Hero): the chosen hero for the game
            map (Map): the chosen map for the game

        Returns
            GameState: the initial game state
        """
        return GameState(player_name, hero, map, debug)
