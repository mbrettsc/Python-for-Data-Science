class calculator:
    """ This class is a calculator that can perform dot product, addition and subtraction on two lists of numbers """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        dot_product = sum([V1[i] * V2[i] for i in range(len(V1))])
        print(f"Dot product is: {dot_product}")
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        add_vector = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"Add Vector is: {add_vector}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        sous_vector = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"Sous Vector is: {sous_vector}")
