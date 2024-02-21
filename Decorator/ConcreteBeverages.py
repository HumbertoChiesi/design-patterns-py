from Decorator.Beverage import Beverage


class Expresso(Beverage):
    def __init__(self):
        self._description = "Expresso"

    def cost(self) -> float:
        return 8.99


class Tea(Beverage):
    def __init__(self):
        self._description = "Tea"

    def cost(self) -> float:
        return 5.99


class Decaf(Beverage):
    def __init__(self):
        self._description = "Decaf"

    def cost(self) -> float:
        return 6.99
