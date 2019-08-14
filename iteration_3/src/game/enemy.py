from .personnage import Personnage

class Enemy(Personnage):

    def __init__(self, name, image, case_enemy, attack_level, life_points):
        self.case_enemy = case_enemy
        self._life_points = life_points
        Personnage.__init__(self, name, image, attack_level, life_points)

    def get_name(self):
        return self.name

    @classmethod
    def get_list_enemies(cls):
        return [cls("Dragons", "\033[34m🐉\033[0m", case_enemy=1, attack_level=4, life_points=15),
                cls("Dragons", "\033[34m🐉\033[0m", case_enemy=2, attack_level=4, life_points=15),
                cls("Dragons", "\033[34m🐉\033[0m", case_enemy=19, attack_level=4, life_points=15),
                cls("Dragons", "\033[34m🐉\033[0m", case_enemy=5, attack_level=4, life_points=15),
                cls("Sorcier", "\033[34m🥢\033[0m", case_enemy=17, attack_level=2,life_points= 9),
                cls("Gobelin", "\033[34m👹\033[0m", case_enemy=18, attack_level=1, life_points=6),
                cls("Sorcier", "\033[34m🥢\033[0m", case_enemy=25,attack_level= 2, life_points=9),
                cls("Gobelin", "\033[34m👹\033[0m", case_enemy=26, attack_level=1, life_points=6)]

    @property
    def life_points(self):
        return self._life_points

    @life_points.setter
    def life_points(self, life_points):
        if life_points < 0:
            self._life_points = 0
        else:
            self._life_points = life_points

    def __repr__(self):
        return self.image