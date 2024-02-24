import pytest


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class SingletonDeco(object):
    __unique_instance = None

    @classmethod
    def get_instance(cls):
        if cls.__unique_instance is None:
            cls.__unique_instance = object.__new__(SingletonDeco)

        return cls.__unique_instance


def test_singleton():
    s1 = Singleton()
    s2 = Singleton()

    assert id(s1) == id(s2)


def test_singleton_decorator():
    s1 = SingletonDeco.get_instance()
    s2 = SingletonDeco.get_instance()

    assert id(s1) == id(s2)


if __name__ == '__main__':
    pytest.main()
