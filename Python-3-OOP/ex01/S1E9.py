from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for Game of Thrones characters"""
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Prototype for die method"""
        pass


class Stark(Character):
    """House Stark of Winterfell"""
    def die(self):
        """Kills the character"""
        self.is_alive = False
