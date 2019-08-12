from .hero import Hero
from .game_map import Map, Ennemies
from .game_state import GameState

class WarriorsAPI(object):
    """the Warriors Game API"""

    def get_heroes(self):
        """
        Called by the client to retrieve the list of available heroes.

        Returns
            list: the list of available heroes

        """
        return [Hero("Guerrier", "💀", 5, 5), Hero("Magicien", "🧙", 3, 8)]


    def get_maps(self):
        """
        Called by the client to retrieve the list of available maps.

        Returns
            list: the list of available maps
        """
        dragons = Ennemies("Dragons", "🐉", [45, 52, 56, 62])
        return [Map("plateau en ligne", 64, dragons), Map("plateau de l'espace", 32, dragons)]


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
