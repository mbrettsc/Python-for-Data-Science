from S1E9 import Character


class Baratheon(Character):
    """House Baratheon of Storm's End"""
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    def die(self):
        self.is_alive = False


class Lannister(Character):
    """House Lannister of Casterly Rock"""

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    def die(self):
        self.is_alive = False

    def create_lannister(first_name: str, is_alive: bool = True):
        return Lannister(first_name, is_alive)
