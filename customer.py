from interfaces import ICustomer
import random
from drink import Drink, Espresso, Americano, Cappuccino, Latte, Mocha


class Customer(ICustomer):
    def __init__(self, name: str, money: float):
        self.name = name
        self.money = money
    
    def choose_drink(self) -> Drink:
        drinks = [Espresso(), Americano(), Cappuccino(), Latte(), Mocha()]
        affordable_drinks = [d for d in drinks if d.price <= self.money]
        if affordable_drinks:
            return random.choice(affordable_drinks)
        return None
    
    def pay(self, amount: float) -> float:
        if self.money >= amount:
            self.money -= amount
            return amount
        return 0
    
    def get_name(self) -> str:
        return self.name


class CustomerGenerator:
    def __init__(self):
        self.names = ["Олександр", "Марія", "Іван", "Оксана", "Андрій", "Наталія", 
                     "Дмитро", "Юлія", "Сергій", "Катерина", "Микола", "Анна",
                     "Василь", "Ірина", "Петро", "Світлана", "Богдан", "Тетяна"]
    
    def generate_customer(self) -> Customer:
        name = random.choice(self.names)
        money = random.uniform(30, 150)
        return Customer(name, money)
