from random import *
from .game_map import *


class GameState(object):

    """
    This interface describes the game state which should be return after each game turn
    """
    def __init__(self, player_name, hero, map):
        self.gamestatus = "IN_PROGRESS"
        self.player_name = player_name
        self.hero = hero
        self.map = map
        self.last_dice = None
        self.current_case = 0
        self.log = []

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

        return"\n" .join(map(str, self.log))

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

        self.log = []
        de = randint(1, 6)
        self.log.append("Jet du dé lancé : %d" % de)

        self.current_case += de
        if self.current_case <= self.get_map().number_of_case:
            self.gamestatus = "IN_PROGRESS"
            self.log.append(self.gamestatus)
            self.log.append("Case n° %d" % self.current_case)
            tab_map_list = self.map.get_map_list()
            tab_map_list_str = list(map(str, tab_map_list))
            tab_map_list_str[self.current_case] += self.hero.image
            self.log.append(tab_map_list_str)
            for objet in self.map.objet:
                if objet.cases == self.current_case:
                    self.log.append("Vous obtenez un/une %s qui donne %s PDV et %s de dégats" % (objet.name, objet.pdv, objet.degats))
            for ennemie in self.map.ennemies:
                if ennemie.cases == self.current_case:
                    self.log.append("Vous recontrez un %s avec %s PDV et %s de degats" % (ennemie.name, ennemie.pdv, ennemie.degats))
        else:
            self.gamestatus = "FINISHED"

        return True
