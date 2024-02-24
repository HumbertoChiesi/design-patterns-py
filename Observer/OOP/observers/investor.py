from Observer.OOP.observers.observer import Observer
from Observer.lib.util import log


class StockTradingCompany(Observer):

    def update(self, data: dict):
        log(f"Received update: {data}")