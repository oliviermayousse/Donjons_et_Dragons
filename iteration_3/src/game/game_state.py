from random import randint
from .game_status import GAME_STATUS
from .ennemi import Ennemi
from .coffre import Coffre

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
        self.plateau_de_jeu = []
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

    def lance_de(self):
        return randint(1, 6)


    def next_turn(self):
        """
        Called by the client to execute a new turn in the game.

        Returns:
            bool: True if the move can be execute, False if move is impossible

        """
        self.log = []
        dice = self.lance_de()
        self.laste_dice = dice
        self.current_case += self.laste_dice
        nbr_case = self.map.number_of_case

        if self.current_case < nbr_case:

            self.log.append("\033[31m================================Nouveau Tour==============================\033[0m")
            self.plateau_de_jeu = self.map.get_creat_map()
            plateau_presentation = list(map(str, self.plateau_de_jeu))
            plateau_presentation[self.current_case-1] += self.hero.image

            self.log.append(f"{self.player_name} le {self.hero.name}.")
            self.log.append(f"PV : {self.hero.life} / Attaque : {self.hero.attack_level}")
            self.log.append(f"tu fait {self.laste_dice}")

            self.log.append(" | ".join(plateau_presentation[self.current_case-1:]))

            if isinstance(self.plateau_de_jeu[self.current_case-1], Ennemi):
                self.log.append(f"Vous rencontrez un {self.plateau_de_jeu[self.current_case-1].name}")
                self.log.append(f"Point d'attaque :  {self.plateau_de_jeu[self.current_case-1].attack_level}")
                self.log.append(f"PV : {self.plateau_de_jeu[self.current_case-1].life}")

                self.hero.combat(self.plateau_de_jeu[self.current_case-1])
                if self.plateau_de_jeu[self.current_case-1].life <= 0:
                    self.log.append(f"tu as tué le {self.plateau_de_jeu[self.current_case-1].name}")
                else:
                    self.log.append(f"{self.plateau_de_jeu[self.current_case-1].name} s'enfuit")
                if self.hero.life <= 0:
                    self.game_status = "GAME_OVER"

            if isinstance(self.plateau_de_jeu[self.current_case-1], Coffre):
                self.log.append(f"Tu trouve un(e) {self.plateau_de_jeu[self.current_case-1].name}")
                self.log.append(f"Bonus attaque :  {self.plateau_de_jeu[self.current_case-1].attack_level}")
                self.log.append(f"Bonus PV : {self.plateau_de_jeu[self.current_case-1].life}")
                self.hero.equipement(self.plateau_de_jeu[self.current_case-1])

                # self.hero.equipement(self.plateau_de_jeu[self.current_case-1])

            self.log.append(f"Vous avez {self.hero.life} PV et {self.hero.attack_level} point d'attaque")

            if self.game_status == "GAME_OVER" or self.game_status == "FINISHED":
                self.log.append(f"{self.game_status}")


        else:
            self.current_case = nbr_case
            self.game_status = "FINISHED"

        return True
