try:
    from solution.models import WarriorsAPI
except ImportError:
    from ..game.warrior_api import WarriorsAPI


class ConsoleUI(object):
    def __init__(self):
        warriors = WarriorsAPI()
        while True:
            choice = self.display_menu()
            if choice == "1":
                self.start_game(warriors)
            elif choice == "2":
                print("")
                print("Good bye :) ")
                print("")
                break

    def start_game(self, warriors):
        # PLAYER NAME
        player_name = input("Enter your name : ")

        # HERO CHOICE
        available_heroes = warriors.get_heroes()
        hero_choices = " | ".join(["(%s) %s" % (i, h.get_name()) for i, h in enumerate(available_heroes, 1)])
        hero_choice = int(input("Choose a hero \n%s \n" % hero_choices))
        hero = available_heroes[hero_choice - 1]

        # MAP CHOICE
        available_maps = warriors.get_maps()
        map_choices = " | ".join(["(%s) %s" % (i, game_map.get_name()) for i, game_map in enumerate(available_maps, 1)])
        map_choice = int(input("Choose a map \n%s \n" % map_choices))
        game_map = available_maps[map_choice - 1]

        game_state = warriors.create_game(player_name, hero, game_map)

        while game_state.get_game_status() == "IN_PROGRESS":
            print(game_state.get_last_log())
            action = input("('Entrer') pour lancer le dé / (Q) pour quitter la partie")
            if action and action.upper() == "Q":
                break
            else:
                game_state.next_turn()
        if game_state.get_game_status() == "GAME_OVER":
            print(game_state.get_last_log())
            print('Tu as perdu!!!!')
        elif game_state.get_game_status() == "FINISHED":
            print(game_state.get_last_log())
            print("Tu as gagné")

    def display_menu(self):
        print("")
        print("================== Python Warriors ==================")
        return input("(1) Start new game  |  (2) Exit game ")


