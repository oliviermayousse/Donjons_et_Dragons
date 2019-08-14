class Ennemie(object):
    def __init__(self, name, image, cases, pdv, degats):
        self.name = name
        self.image = image
        self.cases = cases
        self.pdv = pdv
        self.degats = degats

    def __repr__(self):
        return self.image

    def get_case_ennemie(self):
        return self.cases

    @classmethod
    def get_list_ennemie(cls):

        list_ennemie = [
            cls(name="Dragons", image="🦎", cases=45, pdv=15, degats=4),
            cls(name="Dragons", image="🦎", cases=52, pdv=15, degats=4),
            cls(name="Dragons", image="🦎", cases=56, pdv=15, degats=4),
            cls(name="Dragons", image="🦎", cases=62, pdv=15, degats=4),
            cls(name="Tigre", image="🐅 ", cases=10, pdv=9, degats=2),
            cls(name="Tigre", image="🐅 ", cases=20, pdv=9, degats=2),
            cls(name="Tigre", image="🐅 ", cases=25, pdv=9, degats=2),
            cls(name="Tigre", image="🐅 ", cases=32, pdv=9, degats=2),
            cls(name="Tigre", image="🐅 ", cases=35, pdv=9, degats=2),
            cls(name="Tigre", image="🐅 ", cases=36, pdv=9, degats=2),
            cls(name="Tigre", image="🐅 ", cases=37, pdv=9, degats=2),
            cls(name="Tigre", image="🐅 ", cases=40, pdv=9, degats=2),
            cls(name="Tigre", image="🐅 ", cases=44, pdv=9, degats=2),
            cls(name="Tigre", image="🐅 ", cases=47, pdv=9, degats=2),
            cls(name="Poulet", image="🐔", cases=3, pdv=6, degats=1),
            cls(name="Poulet", image="🐔", cases=6, pdv=6, degats=1),
            cls(name="Poulet", image="🐔", cases=9, pdv=6, degats=1),
            cls(name="Poulet", image="🐔", cases=12, pdv=6, degats=1),
            cls(name="Poulet", image="🐔", cases=15, pdv=6, degats=1),
            cls(name="Poulet", image="🐔", cases=18, pdv=6, degats=1),
            cls(name="Poulet", image="🐔", cases=21, pdv=6, degats=1),
            cls(name="Poulet", image="🐔", cases=24, pdv=6, degats=1),
            cls(name="Poulet", image="🐔", cases=27, pdv=6, degats=1),
            cls(name="Poulet", image="🐔", cases=30, pdv=6, degats=1),
        ]
        return list_ennemie
