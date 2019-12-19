from .base import BaseName, BaseCompetence
import json


class Coffre(BaseName, BaseCompetence):

    def __init__(self, name, image, case, life, attack_level):
        BaseName.__init__(self, name)
        BaseCompetence.__init__(self, image, life, attack_level)
        self.case = case

    @classmethod
    def get_list_coffre(cls):
        with open('src/res/donjons_map.json') as json_file:
            data = json.load(json_file)
        list_coffre = []
        for coffre in data["coffres"]:
            list_coffre.append(cls(coffre["name"], coffre["image"], coffre["case"], coffre["life"], coffre["attack_level"]))

        return list_coffre

    def __repr__(self):
        return self.image
