from random import randint
from .game_map import *

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
        return self.get_player_name()

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
        if self.current_case <= self.map.number_of_case:
            GAMESTATUS = "IN_PROGRESS"
        else:
            GAMESTATUS = "FINISHED"
        # GAMESTATUS = "IN_PROGRESS"
        return GAMESTATUS

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
        plateau_de_jeu = []
        cases_dragons = self.map.get_cases_dragons()
        i = 0
        while i <= (self.map.number_of_case - 1):
            if i == self.current_case:
                plateau_de_jeu.append(self.hero.image)
            elif i in cases_dragons:
                plateau_de_jeu.append(self.ennemies.image)
            else:
                plateau_de_jeu.append(" ")
            i += 1

        return "\n".join([str(self.current_case), self.hero.get_name(), self.hero.image, "|".join(plateau_de_jeu)])

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
        dice = randint(1, 6)
        self.last_dice = dice
        self.current_case += dice
        return True
