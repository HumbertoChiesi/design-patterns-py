from Observer.OOP.observers.investor import Investor
from Observer.OOP.subjects.stocks import StockPlatform


def main():
    platform = StockPlatform()
    investor_1 = Investor("Humberto")
    investor_2 = Investor("Lucas")

    platform.add_observer(investor_1)

    platform.update_stock("ITUB4.SA", 40.5)

    platform.add_observer(investor_2)

    platform.update_stock("B3SA3.SA", 30)

    platform.end_trade_day()

    platform.open_trade_day()


if __name__ == "__main__":
    main()
