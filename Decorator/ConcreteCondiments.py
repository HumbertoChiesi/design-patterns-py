from Decorator.Beverage import Beverage
from Decorator.CondimentDecorator import CondimentDecorator


class Mocha(CondimentDecorator):
    _beverage: Beverage

    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return 1.4 + self._beverage.cost()


class Whip(CondimentDecorator):
    _beverage: Beverage

    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return 2 + self._beverage.cost()


class Milk(CondimentDecorator):
    _beverage: Beverage

    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Milk"

    def cost(self) -> float:
        return 1 + self._beverage.cost()
