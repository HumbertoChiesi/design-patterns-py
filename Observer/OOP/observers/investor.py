from Observer.OOP.observers.observer import Observer
from Observer.lib.util import log


class Investor(Observer):

    def __init__(self, investor_name: str):
        self.name = investor_name

    def update(self, data: dict):
        log(f"Investor {self.name} received update: {data}")
