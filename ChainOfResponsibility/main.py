from __future__ import annotations

import hashlib
from abc import ABC, abstractmethod
from typing import Any, Optional

import bcrypt


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return request


class ReverseHandler(AbstractHandler):
    def handle(self, request: str) -> str:
        return super().handle(request[::-1])


class UpperHandler(AbstractHandler):
    def handle(self, request: str) -> str:
        return super().handle(request.upper())


class HashHandler(AbstractHandler):
    def handle(self, request: str) -> str:
        return super().handle(hashlib.md5(request.encode('utf-8')).hexdigest())


class AddSaltHandler(AbstractHandler):

    def handle(self, request: Any) -> str:
        salt = bcrypt.gensalt(rounds=6).decode('utf-8')
        return super().handle(request + salt)


if __name__ == '__main__':
    reverse = ReverseHandler()
    upper = UpperHandler()
    add_salt = AddSaltHandler()
    hasher = HashHandler()

    reverse.set_next(upper).set_next(add_salt).set_next(hasher)

    print(reverse.handle('senha'))
