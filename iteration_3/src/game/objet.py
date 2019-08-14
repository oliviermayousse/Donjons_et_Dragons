class Objet(object):
    def __init__(self, name, image, cases, pdv, degats):
        self.name = name
        self.image = image
        self.cases = cases
        self.pdv = pdv
        self.degats = degats

    def __repr__(self):
        return self.image

    def get_cases_objet(self):
        return self.cases

    @classmethod
    def get_objet_list(cls):
        list_objet = [
            cls(name="Arc", image="🏹", cases=2, pdv=0, degats=1),
            cls(name="Arc", image="🏹", cases=11, pdv=0, degats=1),
            cls(name="Arc", image="🏹", cases=14, pdv=0, degats=1),
            cls(name="Arc", image="🏹", cases=19, pdv=0, degats=1),
            cls(name="Arc", image="🏹", cases=26, pdv=0, degats=1),
            cls(name="Masse", image="🔨", cases=5, pdv=0, degats=3),
            cls(name="Masse", image="🔨", cases=22, pdv=0, degats=3),
            cls(name="Masse", image="🔨", cases=38, pdv=0, degats=3),
            cls(name="épée", image="⚔️", cases=42, pdv=0, degats=5),
            cls(name="épée", image="⚔️", cases=53, pdv=0, degats=5),
            cls(name="Sort éclair", image="⚡", cases=1, pdv=0, degats=2),
            cls(name="Sort éclair", image="⚡", cases=4, pdv=0, degats=2),
            cls(name="Sort éclair", image="⚡", cases=8, pdv=0, degats=2),
            cls(name="Sort éclair", image="⚡", cases=17, pdv=0, degats=2),
            cls(name="Sort éclair", image="⚡", cases=23, pdv=0, degats=2),
            cls(name="Sort Boule de feu", image="🔥", cases=48, pdv=0, degats=7),
            cls(name="Sort Boule de feu", image="🔥", cases=49, pdv=0, degats=7),
            cls(name="Petite potion", image="🍷", cases=7, pdv=1, degats=0),
            cls(name="Petite potion", image="🍷", cases=13, pdv=1, degats=0),
            cls(name="Petite potion", image="🍷", cases=28, pdv=1, degats=0),
            cls(name="Petite potion", image="🍷", cases=29, pdv=1, degats=0),
            cls(name="Petite potion", image="🍷", cases=33, pdv=1, degats=0),
            cls(name="Potion standards", image="⚗️", cases=31, pdv=2, degats=0),
            cls(name="Potion standards", image="⚗️", cases=39, pdv=2, degats=0),
            cls(name="Potion standards", image="⚗️", cases=43, pdv=2, degats=0),
            cls(name="Grand potion", image="❤️", cases=41, pdv=5, degats=0),
        ]
        return list_objet
