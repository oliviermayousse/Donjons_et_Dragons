from .hero import Hero
from .game_map import Map
from .game_map import Ennemie
from .game_state import GameState
from .game_map import Objet


class WarriorsAPI(object):
    """the Warriors Game API"""

    def get_heroes(self):
        """
        Called by the client to retrieve the list of available heroes.

        Returns
            list: the list of available heroes

        """
        guerrier = Hero(name="Guerrier", image="🧙", current_life_points="5", attaque="5")
        magicien = Hero(name="Magicien", image="🧙", current_life_points="3", attaque="8")
        heroes_list = [guerrier, magicien]
        return heroes_list

    def get_maps(self):
        """
        Called by the client to retrieve the list of available maps.

        Returns
            list: the list of available maps
        """
        list_ennemie = [
            Ennemie(name="Dragons", image="🦎", cases=45, pdv="15", degats="4"),
            Ennemie(name="Dragons", image="🦎", cases=52, pdv="15", degats="4"),
            Ennemie(name="Dragons", image="🦎", cases=56, pdv="15", degats="4"),
            Ennemie(name="Dragons", image="🦎", cases=62, pdv="15", degats="4"),
            Ennemie(name="Tigre", image="🐅 ", cases=10, pdv="9", degats="2"),
            Ennemie(name="Tigre", image="🐅 ", cases=20, pdv="9", degats="2"),
            Ennemie(name="Tigre", image="🐅 ", cases=25, pdv="9", degats="2"),
            Ennemie(name="Tigre", image="🐅 ", cases=32, pdv="9", degats="2"),
            Ennemie(name="Tigre", image="🐅 ", cases=35, pdv="9", degats="2"),
            Ennemie(name="Tigre", image="🐅 ", cases=36, pdv="9", degats="2"),
            Ennemie(name="Tigre", image="🐅 ", cases=37, pdv="9", degats="2"),
            Ennemie(name="Tigre", image="🐅 ", cases=40, pdv="9", degats="2"),
            Ennemie(name="Tigre", image="🐅 ", cases=44, pdv="9", degats="2"),
            Ennemie(name="Tigre", image="🐅 ", cases=47, pdv="9", degats="2"),
            Ennemie(name="Poulet", image="🐔", cases=3, pdv="6", degats="1"),
            Ennemie(name="Poulet", image="🐔", cases=6, pdv="6", degats="1"),
            Ennemie(name="Poulet", image="🐔", cases=9, pdv="6", degats="1"),
            Ennemie(name="Poulet", image="🐔", cases=12, pdv="6", degats="1"),
            Ennemie(name="Poulet", image="🐔", cases=15, pdv="6", degats="1"),
            Ennemie(name="Poulet", image="🐔", cases=18, pdv="6", degats="1"),
            Ennemie(name="Poulet", image="🐔", cases=21, pdv="6", degats="1"),
            Ennemie(name="Poulet", image="🐔", cases=24, pdv="6", degats="1"),
            Ennemie(name="Poulet", image="🐔", cases=27, pdv="6", degats="1"),
            Ennemie(name="Poulet", image="🐔", cases=30, pdv="6", degats="1"),
        ]

        list_objet = [
            Objet(name="Arc", image="🏹", cases=2, pdv="0", degats="1"),
            Objet(name="Arc", image="🏹", cases=11, pdv="0", degats="1"),
            Objet(name="Arc", image="🏹", cases=14, pdv="0", degats="1"),
            Objet(name="Arc", image="🏹", cases=19, pdv="0", degats="1"),
            Objet(name="Arc", image="🏹", cases=26, pdv="0", degats="1"),
            Objet(name="Masse", image="🔨", cases=5, pdv="0", degats="3"),
            Objet(name="Masse", image="🔨", cases=22, pdv="0", degats="3"),
            Objet(name="Masse", image="🔨", cases=38, pdv="0", degats="3"),
            Objet(name="épée", image="⚔️", cases=42, pdv="0", degats="5"),
            Objet(name="épée", image="⚔️", cases=53, pdv="0", degats="5"),
            Objet(name="Sort éclair", image="⚡", cases=1, pdv="0", degats="2"),
            Objet(name="Sort éclair", image="⚡", cases=4, pdv="0", degats="2"),
            Objet(name="Sort éclair", image="⚡", cases=8, pdv="0", degats="2"),
            Objet(name="Sort éclair", image="⚡", cases=17, pdv="0", degats="2"),
            Objet(name="Sort éclair", image="⚡", cases=23, pdv="0", degats="2"),
            Objet(name="Sort Boule de feu", image="🔥", cases=48, pdv="0", degats="7"),
            Objet(name="Sort Boule de feu", image="🔥", cases=49, pdv="0", degats="7"),
            Objet(name="Petite potion", image="🍷", cases=7, pdv="1", degats="0"),
            Objet(name="Petite potion", image="🍷", cases=13, pdv="1", degats="0"),
            Objet(name="Petite potion", image="🍷", cases=28, pdv="1", degats="0"),
            Objet(name="Petite potion", image="🍷", cases=29, pdv="1", degats="0"),
            Objet(name="Petite potion", image="🍷", cases=33, pdv="1", degats="0"),
            Objet(name="Potion standards", image="⚗️", cases=31, pdv="2", degats="0"),
            Objet(name="Potion standards", image="⚗️", cases=39, pdv="2", degats="0"),
            Objet(name="Potion standards", image="⚗️", cases=43, pdv="2", degats="0"),
            Objet(name="Grand potion", image="❤️", cases=41, pdv="5", degats="0"),
        ]

        foret = Map(name="Forêt", number_of_case=64, ennemies=list_ennemie, objet=list_objet)
        chateau = Map(name="Chateau", number_of_case=64, ennemies=list_ennemie, objet=list_objet)

        list_map = [foret, chateau]

        return list_map

    def create_game(self, player_name, hero, map):
        """Called by the client to create a new game

        Args:
            player_name (str): the name of the player
            hero (Hero): the chosen hero for the game
            map (Map): the chosen map for the game

        Returns
            GameState: the initial game state
        """
        new_game = GameState(player_name, hero, map)

        return new_game


