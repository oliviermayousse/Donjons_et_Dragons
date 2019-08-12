class Map(object):
    """
    This interface contains all data needed by the client about the game map
    """

    def __init__(self, name, number_of_case):
        self.name = name
        self.number_of_case = number_of_case

    def get_name(self):
        """
        Returns
            str: The name of the map
        """

        return self.name

    def get_number_of_case(self):
        """
        Returns
            int: the number of case
        """
        self.number_of_case = 64
        return self.number_of_case


class Ennemeies(object):
    def __init__(self, name, image, cases):
        self.name = name
        self.image = image
        self.cases = cases

    def get_cases_ennemies(self):
        return self.cases


dragons = Ennemeies(name="Dragons", image="🦎", cases=[45, 52, 56, 62])
tigre = Ennemeies(name="Tigre", image="🐅 ", cases=[10, 20, 25, 32, 35, 36, 37, 40, 44, 47])
poulet = Ennemeies(name="Poulet", image="🐔", cases=[3, 6,  9 , 12, 15, 18, 21, 24, 27, 30])


class Objet(object):
    def __init__(self, name, image, cases):
        self.name = name
        self.image = image
        self.cases = cases

    def get_cases_objet(self):
        return self.cases


arc = Objet(name="Arc", image="🏹", cases=[2, 11, 14, 19, 26])
masse = Objet(name="Masse", image="🔨", cases=[5, 22, 38])
epee = Objet(name="épée", image="⚔️", cases=[42, 53])
sort_eclair = Objet(name="Sort éclair", image="⚡", cases=[1, 4, 8, 17, 23])
sort_fireball = Objet(name="Sort Boule de feu", image="🔥", cases=[48, 49])
petite_potion = Objet(name="Petite potion", image="🍷", cases=[7, 13, 28, 29, 33])
potion_standards = Objet(name="Potion standards", image="⚗️", cases=[31, 39, 43])
grande_potion = Objet(name="Grand potion", image="✨", cases=[41])
