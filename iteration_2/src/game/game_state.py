from random import *

taille_plateau_MAX = 65


class GameState(object):

    """
    This interface describes the game state which should be return after each game turn
    """
    def __init__(self, player_name, hero, map):
        self.player_name = player_name
        self.hero = hero
        self.map = map
        self.last_dice = None
        self.current_case = 0

    def get_player_name(self):
        """
        Returns:
            str: The player name
        """

        return self.player_name

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
        if self.current_case <= 64:
            self.gamestatus = "IN_PROGRESS"
        else:
            self.gamestatus = "FINISHED"

        return self.gamestatus

    def get_hero(self):
        """
        Returns:
            Hero: the current hero
        """
        return self.hero

    def get_map(self):
        """
        Returns:
            Map: the current map
        """
        return self.map

    def get_last_log(self):
        """
        Returns:
            str: the last log of the game. This log is displayed by the client after each game turn
        """
        plateau = []

        for i in range(1, taille_plateau_MAX):
            if i == self.current_case:
                plateau.append("X")
            # elif i == 45 or i == 52 or i == 56 or i == 62:
            #     plateau.append("🦎")
            else:
                plateau.append("_")

        return self.last_dice, self.current_case, plateau

    def get_current_case(self):
        """
        Returns:
            int: the current case index (base 1)
        """

        return self.current_case

    def next_turn(self):
        """
        Called by the client to execute a new turn in the game.

        Returns:
            bool: True if the move can be execute, False if move is impossible

        """
        de = randint(1, 6)
        self.last_dice = de
        self.current_case += self.last_dice
        return True
