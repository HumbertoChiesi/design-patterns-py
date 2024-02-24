from Observer.OOP.observers.observer import Observer
from Observer.OOP.subjects.abstract_subject import Subject
from Observer.lib.util import get_stocks


class StockPlatform(Subject):
    stocks: dict = get_stocks()
    stock_status: str = "Open"
    _observers = list()

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        if observer not in self._observers:
            raise Exception("Observer does not exist")

        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(f"status updated, now: {self.stock_status}")

    def notify_stock_update(self, stock_name: str):
        for observer in self._observers:
            observer.update({stock_name: self.stocks[stock_name]})

    def create_stock(self, stock_name: str, stock_price: float):
        if stock_name in self.stocks:
            raise Exception("Stock already exists")

        self.stocks[stock_name] = stock_price

    def update_stock(self, stock_name: str, stock_price: float):
        if stock_name not in self.stocks:
            raise Exception("Stock does not exists")

        self.stocks[stock_name] = stock_price
        self.notify_stock_update(stock_name)

    def end_trade_day(self):
        self.stock_status = "Closed"
        self.notify()

    def open_trade_day(self):
        self.stock_status = "Open"
        self.notify()

