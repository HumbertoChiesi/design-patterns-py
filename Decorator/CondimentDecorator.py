from abc import abstractmethod
from Decorator.Beverage import Beverage


class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self):
        raise NotImplementedError
