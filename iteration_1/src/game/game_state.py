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
        self.log = []

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
        last_log = "\n".join(map(str, self.log))
        return last_log

    def get_current_case(self):
        """
        Returns:
            int: the current case index (base 1)
        """
        return self.current_case

    def next_turn(self):
        """
        Called by the client to execute a new turn in the game.
        """
        self.log = []
        self.log.append("Nom du Héro : %s %s" % (self.hero.nom, self.hero.image))
        self.log.append("Point de vie : %s" %self.hero.life)
        self.log.append("Point d'attaque : %s" %self.hero.attack_level)
        dice = randint(1, 6)
        self.last_dice = dice
        self.current_case += dice
        self.log.append("résultat jet de dé : %s" %dice)

        i = 0
        while i < len(self.map.list_enemies):
            if self.current_case == self.map.list_enemies[i].case_enemy:
                self.log.append("vous rencontrez un ennemi : %s %s POINT D'ATTAQUE : %s POINT DE VIE : %s" %(self.map.list_enemies[i].name_enemy,
                                                                                           self.map.list_enemies[i].image_enemy,
                                                                                           self.map.list_enemies[i].attack_points,
                                                                                           self.map.list_enemies[i].life_points))
            i += 1

        i = 0
        while i < len(self.map.list_caisses_surprises):
            if self.current_case == self.map.list_caisses_surprises[i].case_surprise:
                self.log.append("vous rencontrez une caisse surprise : %s %s" % (self.map.list_caisses_surprises[i].nom_surprise, self.map.list_caisses_surprises[i].image_surprise))
            i += 1

        plateau_de_jeu = self.map.create_map()
        i = 0
        while i <= (self.map.number_of_case - 1):
            if i == self.current_case:
                plateau_de_jeu[i] = self.hero.image
            i += 1
        self.log.append("|".join(plateau_de_jeu))
        return self.log