from random import randint
from .game_status import GAME_STATUS
import csv

class GameState(object):
    """
    This interface describes the game state which should be return after each game turn
    """
    def __init__(self, player_name, hero, map, debug):
        self.player_name = player_name
        self.hero = hero
        self.map = map
        self.laste_dice = None
        self.current_case = 0
        self.game_status = GAME_STATUS[0]
        self.plateau_de_jeu = []
        self.log = []
        self.debug = debug
        if debug == True:
            with open('../res/dicescenar.txt') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                self.dicescenar = []
                for row in csv_reader:
                    for dice in row:
                        self.dicescenar.append(dice)


            self.debug_dice = "XXX"

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

        return "\n".join(map(str, self.log))

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
        if self.debug:
            self.laste_dice = self.dicescenar[0]
            self.dicescenar.pop(0)
        self.laste_dice = randint(1, 6)
        self.current_case += self.laste_dice

        self.plateau_de_jeu = self.map.get_creat_map()
        nbr_case = self.map.number_of_case
        for i in range(0, nbr_case - 1):
            if i == self.current_case:
                self.plateau_de_jeu[i] += self.hero.image
        self.log.append(f"{self.player_name} le {self.hero.name} avance de {self.laste_dice} case(s)")
        for ennemi in self.map.liste_ennemi:
            if ennemi.case == self.current_case:
                self.log.append(f"Vous rencontrez un {ennemi.name} qui as {ennemi.attack} point attaque et {ennemi.life} PV")
        for coffre in self.map.liste_coffres:
            if coffre.case == self.current_case:
                self.log.append(f"Vous trouvez un {coffre.name} qui vous donne {coffre.attack} point attaque et {coffre.life} PV")
        self.log.append(f"Vous avez {self.hero.life} PV et {self.hero.attack_level} point d'attaque")
        self.log.append(" - ".join(self.plateau_de_jeu[self.current_case:self.current_case+10]))

        return True
