from abc import ABC, abstractmethod
from typing import List


class Repository[T](ABC):
    @abstractmethod
    def get(self, id: str) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[T]:
        raise NotImplementedError

    @abstractmethod
    def add(self, **kwargs: object) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedError
