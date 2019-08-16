from random import *
from .objet import *
from .hero import *
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

    def lancer_de_de(self):
        de = randint(1, 6)
        return de

    def next_turn(self):
        """
        Called by the client to execute a new turn in the game.

        Returns:
            bool: True if the move can be execute, False if move is impossible

        """

        self.log = []
        de = self.lancer_de_de()
        self.log.append("Jet du dé lancé : %d" % de)
        self.current_case += de
        if self.current_case <= self.get_map().number_of_case:
            self.gamestatus = "IN_PROGRESS"
            self.log.append(self.gamestatus)
            self.log.append("Case n° %d" % self.current_case)
            tab_map_list = self.map.get_map_list()
            tab_map_list_str = list(map(str, tab_map_list))
            tab_map_list_str[self.current_case-1] += self.hero.image
            self.log.append(tab_map_list_str)
            if isinstance(tab_map_list[self.current_case-1], Objet):
                self.log.append("Vous trouvez un/une %s qui donne %s PDV et %s de dégats" % (tab_map_list[self.current_case-1].name, tab_map_list[self.current_case-1].pdv, tab_map_list[self.current_case-1].degats))
                if self.hero.do_equip_or_not(tab_map_list[self.current_case-1]) is True:
                    self.log.append("L'objet est équipable")
                    self.hero.ajout_equipement(tab_map_list[self.current_case-1])
                    self.log.append("%s le %s" % (self.player_name, self.hero.name))
                    self.log.append("Pdv actuel = %s" % self.hero.current_life_points)
                    self.log.append("Points d'attaque actuel = %s" % self.hero.attaque)
                else:
                    self.log.append("Impossible d'équiper l'objet")
                    self.log.append("%s le %s" % (self.player_name, self.hero.name))
                    self.log.append("Pdv actuel = %s" % self.hero.current_life_points)
                    self.log.append("Points d'attaque actuel = %s" % self.hero.attaque)
            if isinstance(tab_map_list[self.current_case-1], Ennemie):
                self.log.append("Vous recontrez un %s avec %s PDV et %s de degats" % (tab_map_list[self.current_case-1].name, tab_map_list[self.current_case-1].pdv, tab_map_list[self.current_case-1].degats))
                self.hero.combat(tab_map_list[self.current_case-1])
                self.log.append("%s le %s" % (self.player_name, self.hero.name))
                self.log.append("Pdv actuel = %s" % self.hero.current_life_points)
                self.log.append("Points d'attaque actuel = %s" % self.hero.attaque)
                if self.hero.current_life_points <= 0:
                    self.log.append("Pdv actuel = %s PERDU :(" % self.hero.current_life_points)
                    self.gamestatus = "GAME_OVER"
                    return False
        else:
            self.gamestatus = "FINISHED"
            return False

        return True
