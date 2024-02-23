from Decorator.ConcreteBeverages import Expresso
from Decorator.ConcreteCondiments import Milk, Whip, Mocha

if __name__ == '__main__':
    beverage = Expresso()

    print(f"ordered beverage: {beverage.get_description()}\n cost: {beverage.cost()}\n")

    beverage = Expresso()
    beverage = Milk(beverage)
    beverage = Milk(beverage)
    beverage = Whip(beverage)
    beverage = Mocha(beverage)

    print(f"ordered beverage: {beverage.get_description()}\n cost: {beverage.cost()}\n")
