from interfaces import IOrder
from drink import Drink


class Order(IOrder):
    def __init__(self, drink: Drink):
        self.drink = drink
    
    def get_drink(self) -> Drink:
        return self.drink
    
    def get_total_price(self) -> float:
        return self.drink.price
