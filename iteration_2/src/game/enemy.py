
class Enemy(object):

    def __init__(self, name, image_enemy, case_enemy, attack_points, life_points):
        self.name_enemy = name
        self.image_enemy = image_enemy
        self.case_enemy = case_enemy
        self.attack_points = attack_points
        self.life_points = life_points

    def get_name(self):
        return self.name_enemy

    @classmethod
    def get_list_enemies(cls):
        return [cls("Dragons", "\033[34m🐉\033[0m", 1, 4, 15),
                cls("Dragons", "\033[34m🐉\033[0m", 2, 4, 15),
                cls("Dragons", "\033[34m🐉\033[0m", 19, 4, 15),
                cls("Dragons", "\033[34m🐉\033[0m", 5, 4, 15),
                cls("Sorcier", "\033[34m🥢\033[0m", 17, 2, 9),
                cls("Gobelin", "\033[34m👹\033[0m", 18, 1, 6),
                cls("Dragons", "\033[34m🐉\033[0m", 6, 4, 15),
                cls("Sorcier", "\033[34m🥢\033[0m", 25, 2, 9),
                cls("Gobelin", "\033[34m👹\033[0m", 26, 1, 6)]

    # print"\033[34mThis is blue\033[0m"

    def __repr__(self):
        return self.image_enemy