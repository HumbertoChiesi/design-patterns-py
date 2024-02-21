from abc import ABC, abstractmethod


class Beverage(ABC):
    _description: str = "abstract Beverage"

    def get_description(self):
        return self._description

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError
