# TODO create class PythagoreanTheorem
import math


class PythagoreanTheorem:
    def __init__(self, num1, num2):
        self.n1 = num1
        self.n2 = num2

    def hypotenuse(self):
        return math.sqrt((self.n1**2)+(self.n2**2))

if __name__ == "__main__":
    # create PythagoreanTheorem below this
    pass