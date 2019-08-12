from random import randint
from .game_status import GAME_STATUS

class GameState(object):
    """
    This interface describes the game state which should be return after each game turn
    """
    def __init__(self, player_name, hero, map):
        self.player_name = player_name
        self.hero = hero
        self.map = map
        self.laste_dice = None
        self.current_case = 0
        self.game_status = GAME_STATUS[0]

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

        return self.game_status

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
        tableau = []
        nbr_case = self.map.number_of_case
        for i in range(1, nbr_case):
            if i == self.current_case:
                tableau.append(self.hero.image)
            else:
                tableau.append('.')

        return "\n".join([str(self.current_case), self.hero.image, self.hero.name, ' - '.join(tableau[self.current_case-1:self.current_case+10])])

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
        self.laste_dice = randint(1, 6)
        self.current_case += self.laste_dice

        return self.current_case
