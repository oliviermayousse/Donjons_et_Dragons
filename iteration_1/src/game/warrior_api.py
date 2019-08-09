class WarriorsAPI(object):
    """the Warriors Game API"""

    def get_heroes(self):
        """
        Called by the client to retrieve the list of available heroes.

        Returns
            list: the list of available heroes

        """
        return

    def get_maps(self):
        """
        Called by the client to retrieve the list of available maps.

        Returns
            list: the list of available maps
        """
        return

    def create_game(self, player_name, hero, map):
        """Called by the client to create a new game

        Args:
            player_name (str): the name of the player
            hero (Hero): the chosen hero for the game
            map (Map): the chosen map for the game

        Returns
            GameState: the initial game state
        """
        return
