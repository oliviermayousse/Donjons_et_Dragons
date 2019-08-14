from .hero import Hero
from .game_map import Map
from .enemy import Enemy
from .caissesurprise import CaisseSurprise
from .game_state import GameState
from random import randint

class WarriorsAPI(object):
    """the Warriors Game API"""

    def get_heroes(self):
        """
        Called by the client to retrieve the list of available heroes.

        Returns
            list: the list of available heroes

        """
        return [Hero("Guerrier","\033[31m💀\033[0m", life_points = 5, attack_level = 5, max_life_points = 10, max_attack_level = 10),
                Hero("Magicien", "\033[31m🧙\033[0m", life_points = 3, attack_level = 8, max_life_points = 6, max_attack_level = 15)]



    def get_maps(self):
        """
        Called by the client to retrieve the list of available maps.

        Returns
            list: the list of available maps

        """
        list_enemies = Enemy.get_list_enemies()
        list_caisses_surprises = CaisseSurprise.get_list_caisses_surprises()
        return [Map("plateau en ligne", 30, list_enemies, list_caisses_surprises),
                Map("plateau de l'espace", 32, list_enemies, list_caisses_surprises)]


    def create_game(self, player_name, hero, map):
        """Called by the client to create a new game

        Args:
            player_name (str): the name of the player
            hero (Hero): the chosen hero for the game
            map (Map): the chosen map for the game

        Returns
            GameState: the initial game state
        """
        initialisation_jeu = GameState(player_name, hero, map)

        return initialisation_jeu
