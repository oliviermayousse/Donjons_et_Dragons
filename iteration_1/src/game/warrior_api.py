from .hero import Hero
from .game_map import Map, Enemy, CaisseSurprise
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

    def get_list_enemies(self):
        return [Enemy("Dragons", "🐉", 21, 4, 15),
                Enemy("Dragons", "🐉", 2, 4, 15),
                Enemy("Dragons", "🐉", 19, 4, 15),
                Enemy("Dragons", "🐉", 5, 4, 15),
                Enemy("Sorcier", "🥢", 17, 2, 9),
                Enemy("Gobelin", "👹", 18, 1, 6),
                Enemy("Dragons", "🐉", 6, 4, 15),
                Enemy("Sorcier", "🥢", 25, 2, 9),
                Enemy("Gobelin", "👹", 26, 1, 6)
                ]


    def get_list_caisses_surprises(self):
        return [CaisseSurprise("Arc", "🏹", 3, 1, 0),
                CaisseSurprise("Potion de vie mineure", "🧴🧴🧴🧴🧴🍾", 7, 0, 1),
                CaisseSurprise("grande potion de vie", "🧴🧴🧴🧴🧴🍾", 11, 0, 5),
                CaisseSurprise("Potion de vie standard", "🧴🧴🧴🧴🧴🍾", 15, 0, 2),
                CaisseSurprise("Massue", "🔨", 8, 3, 0),
                CaisseSurprise("Epée", "⚔️", 10, 5, 0)]

    def get_maps(self):
        """
        Called by the client to retrieve the list of available maps.

        Returns
            list: the list of available maps

        """
        list_enemies = self.get_list_enemies()
        list_caisses_surprises = self.get_list_caisses_surprises()
        return [Map("plateau en ligne", 30,list_enemies, list_caisses_surprises),
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
