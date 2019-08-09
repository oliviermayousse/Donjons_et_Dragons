class GameState(object):
    """
    This interface describes the game state which should be return after each game turn
    """

    def get_player_name(self):
        """
        Returns:
            str: The player name
        """
        return

    def get_game_id(self):
        """
        Returns:
            int: the game unique ID
        """
        return

    def get_game_status(self):
        """
        Returns:
            str: the game status
        """
        return

    def get_hero(self):
        """
        Returns:
            Hero: the current hero
        """
        return

    def get_map(self):
        """
        Returns:
            Map: the current map
        """
        return

    def get_last_log(self):
        """
        Returns:
            str: the last log of the game. This log is displayed by the client after each game turn
        """
        return

    def get_current_case(self):
        """
        Returns:
            int: the current case index (base 1)
        """
        return

    def next_turn(self):
        """
        Called by the client to execute a new turn in the game.

        Returns:
            bool: True if the move can be execute, False if move is impossible

        """
        return
