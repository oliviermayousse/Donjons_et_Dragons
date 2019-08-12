from .hero import Hero
from .game_map import Map
from .game_state import GameState


class WarriorsAPI(object):
    """the Warriors Game API"""

    def get_heroes(self):
        """
        Called by the client to retrieve the list of available heroes.

        Returns
            list: the list of available heroes

        """
        guerrier = Hero(name="Guerrier", current_life_points="5", attaque="5")
        magicien = Hero(name="Magicien", current_life_points="3", attaque="8")
        heroes_list = [guerrier, magicien]
        return heroes_list

    def get_maps(self):
        """
        Called by the client to retrieve the list of available maps.

        Returns
            list: the list of available maps
        """
        foret = Map(name="Forêt", number_of_case=64)
        chateau = Map(name="Chateau", number_of_case=64)
        list_map = [foret, chateau]

        return list_map

    def create_game(self, player_name, hero, map):
        """Called by the client to create a new game

        Args:
            player_name (str): the name of the player
            hero (Hero): the chosen hero for the game
            map (Map): the chosen map for the game

        Returns
            GameState: the initial game state
        """
        new_game = GameState(player_name, hero, map)

        return new_game


