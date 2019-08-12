from .hero import Hero
from .game_map import Map
from .game_state import GameState
from .ennemi import Ennemi
from .coffre import Coffre
from random import randint


class WarriorsAPI(object):
    """the Warriors Game API"""

    def get_heroes(self):
        """
        Called by the client to retrieve the list of available heroes.

        Returns
            list: the list of available heroes

        """

        return [Hero("Warrior", '💪', 5, 5), Hero("Wizard",'🧙', 3, 8)]

    def get_maps(self):
        """
        Called by the client to retrieve the list of available maps.

        Returns
            list: the list of available maps
        """

        list_ennemi = [
            Ennemi("Dragon", "🐉", 45, 15, 4),
            Ennemi("Dragon", "🐉", 52, 15, 4),
            Ennemi("Dragon", "🐉", 56, 15, 4),
            Ennemi("Dragon", "🐉", 62, 15, 4),
            Ennemi("Sorciers", "🌒", 10, 9, 2),
            Ennemi("Sorciers", "🌒", 20, 9, 2),
            Ennemi("Sorciers", "🌒", 25, 9, 2),
            Ennemi("Sorciers", "🌒", 32, 9, 2),
            Ennemi("Sorciers", "🌒", 35, 9, 2),
            Ennemi("Sorciers", "🌒", 36, 9, 2),
            Ennemi("Sorciers", "🌒", 37, 9, 2),
            Ennemi("Sorciers", "🌒", 40, 9, 2),
            Ennemi("Sorciers", "🌒", 44, 9, 2),
            Ennemi("Sorciers", "🌒", 47, 9, 2),
            Ennemi("Gobelins", "🧟", 3, 6, 1),
            Ennemi("Gobelins", "🧟", 6, 6, 1),
            Ennemi("Gobelins", "🧟", 9, 6, 1),
            Ennemi("Gobelins", "🧟", 12, 6, 1),
            Ennemi("Gobelins", "🧟", 15, 6, 1),
            Ennemi("Gobelins", "🧟", 18, 6, 1),
            Ennemi("Gobelins", "🧟", 21, 6, 1),
            Ennemi("Gobelins", "🧟", 24, 6, 1),
            Ennemi("Gobelins", "🧟", 27, 6, 1),
            Ennemi("Gobelins", "🧟", 30, 6, 1),
        ]

        list_coffre = [
            Coffre("Arc", "🏹", 2, 0, 1),
            Coffre("Arc", "🏹", 11, 0, 1),
            Coffre("Arc", "🏹", 14, 0, 1),
            Coffre("Arc", "🏹", 19, 0, 1),
            Coffre("Arc", "🏹", 26, 0, 1),
            Coffre("Massue", "🔨", 5, 0, 3),
            Coffre("Massue", "🔨", 22, 0, 3),
            Coffre("Massue", "🔨", 38, 0, 3),
            Coffre("Epée", "⚔️", 42, 0, 5),
            Coffre("Epée", "⚔️", 53, 0, 5),
            Coffre("Eclair", "⚡️️", 1, 0, 2),
            Coffre("Eclair", "⚡️️", 4, 0, 2),
            Coffre("Eclair", "⚡️️", 8, 0, 2),
            Coffre("Eclair", "⚡️️", 17, 0, 2),
            Coffre("Eclair", "⚡️️", 23, 0, 2),
            Coffre("Boules de feu", "💥️️️", 48, 0, 7),
            Coffre("Boules de feu", "💥️️️", 49, 0, 7),
            Coffre("Potion  de vie mineures", "❤️️️️", 7, 1, 0),
            Coffre("Potion  de vie mineures", "❤️️️️", 13, 1, 0),
            Coffre("Potion  de vie mineures", "❤️️️️", 28, 1, 0),
            Coffre("Potion  de vie mineures", "❤️️️️", 29, 1, 0),
            Coffre("Potion  de vie mineures", "❤️️️️", 33, 1, 0),
            Coffre("Potion de vie standard", "💕️️️️", 31, 2, 0),
            Coffre("Potion de vie standard", "💕️️️️", 39, 2, 0),
            Coffre("Potion de vie standard", "💕️️️️", 43, 2, 0),
            Coffre("Potion de vie standard", "💖", 41, 5, 0),
        ]

        list_maps = [Map("Donjon", 64, list_ennemi, list_coffre)]

        return list_maps

    def create_game(self, player_name, hero, map):
        """Called by the client to create a new game

        Args:
            player_name (str): the name of the player
            hero (Hero): the chosen hero for the game
            map (Map): the chosen map for the game

        Returns
            GameState: the initial game state
        """
        return GameState(player_name, hero, map)
