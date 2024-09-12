from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King of the Seven Kingdoms"""

    def __init__(self, first_name: str, is_alive: bool = True):
        Lannister.__init__(self, first_name, is_alive)
        Baratheon.__init__(self, first_name, is_alive)


    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, value: str):
        self._eyes = value

    @property
    def hairs(self):
        return self._hairs

    @hairs.setter
    def hairs(self, value: str):
        self._hairs = value

    def get_eyes(self):
        return self.eyes
    
    def set_eyes(self, value: str):
        self.eyes = value

    def get_hairs(self):
        return self.hairs

    def set_hairs(self, value: str):
        self.hairs = value

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()
