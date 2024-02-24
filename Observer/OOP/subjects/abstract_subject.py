from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def notify(self):
        raise NotImplementedError

    @abstractmethod
    def add_observer(self, observer):
        raise NotImplementedError

    @abstractmethod
    def remove_observer(self, observer):
        raise NotImplementedError
