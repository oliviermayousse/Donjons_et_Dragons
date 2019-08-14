
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
        return [cls("Dragons", "\033[34m🐉\033[0m", case_enemy=1, attack_points=4, life_points=15),
                cls("Dragons", "\033[34m🐉\033[0m", case_enemy=2, attack_points=4, life_points=15),
                cls("Dragons", "\033[34m🐉\033[0m", case_enemy=19, attack_points=4, life_points=15),
                cls("Dragons", "\033[34m🐉\033[0m", case_enemy=5, attack_points=4, life_points=15),
                cls("Sorcier", "\033[34m🥢\033[0m", case_enemy=17, attack_points=2,life_points= 9),
                cls("Gobelin", "\033[34m👹\033[0m", case_enemy=18, attack_points=1, life_points=6),
                cls("Sorcier", "\033[34m🥢\033[0m", case_enemy=25,attack_points= 2, life_points=9),
                cls("Gobelin", "\033[34m👹\033[0m", case_enemy=26, attack_points=1, life_points=6)]

    def __repr__(self):
        return self.image_enemy