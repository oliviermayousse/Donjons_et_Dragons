from .base import BaseName, BaseCompetence
import json


class Ennemi(BaseName, BaseCompetence):

    def __init__(self, name, image, case, life, attack_level):
        BaseName.__init__(self, name)
        BaseCompetence.__init__(self, image, life, attack_level)
        self.case = case

    @classmethod
    def get_list_ennemi(cls):
        with open('src/res/donjons_map.json') as json_file:
            data = json.load(json_file)
        list_ennemi = []
        for enemy in data["enemies"]:
            list_ennemi.append(cls(enemy["name"],enemy["image"],enemy["case"], enemy["life"], enemy["attack_level"]))

        return list_ennemi

    def __repr__(self):
        return self.image
