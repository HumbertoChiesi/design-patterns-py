from abc import abstractmethod, ABC


class Strategy(ABC):
    @abstractmethod
    def get_price(self, a: float) -> float:
        raise NotImplementedError


class NormalStrategy(Strategy):
    def get_price(self, a: float) -> float:
        return a


class WeekendStrategy(Strategy):

    def get_price(self, a: float) -> float:
        return a * 1.2


class WeekdaysLunchStrategy(Strategy):

    def get_price(self, a: float) -> float:
        return a * 0.8


class Consumer:
    def __init__(self):
        self.strategy: Strategy
        self.bill: float = 0

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self, a: float):
        self.bill = self.strategy.get_price(a)


def main():
    wk_strategy = WeekendStrategy()
    wk_days_strategy = WeekdaysLunchStrategy()
    normal_strategy = NormalStrategy()
    consumer = Consumer()

    consumer.set_strategy(normal_strategy)
    consumer.execute_strategy(20)

    print(consumer.bill)

    consumer.set_strategy(wk_strategy)
    consumer.execute_strategy(20)

    print(consumer.bill)

    consumer.set_strategy(wk_days_strategy)
    consumer.execute_strategy(20)

    print(consumer.bill)


if __name__ == '__main__':
    main()
