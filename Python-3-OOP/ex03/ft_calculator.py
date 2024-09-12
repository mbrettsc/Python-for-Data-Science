class calculator:
    """ This class is a calculator that can perform basic operations on a list of numbers """
    def __init__(self, object):
        self.object = object

    def __add__(self, object) -> None:
        self.object = [object + i for i in self.object]
        print(self.object)
    def __mul__(self, object) -> None:
        self.object = [object * i for i in self.object]
        print(self.object)
    def __sub__(self, object) -> None:
        self.object = [i - object for i in self.object]
        print(self.object)
    def __truediv__(self, object) -> None:
        if object == 0:
            print("Division by zero is not allowed")
            return
        self.object = [i / object for i in self.object]
        print(self.object)
