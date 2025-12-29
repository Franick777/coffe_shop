from abc import ABC, abstractmethod
from typing import Dict


class Drink(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    @abstractmethod
    def get_recipe(self) -> Dict[str, int]:
        pass


class Espresso(Drink):
    def __init__(self):
        super().__init__("Еспресо", 35)
    
    def get_recipe(self) -> Dict[str, int]:
        return {"Кава": 20, "Вода": 30}


class Americano(Drink):
    def __init__(self):
        super().__init__("Американо", 40)
    
    def get_recipe(self) -> Dict[str, int]:
        return {"Кава": 20, "Вода": 120}


class Cappuccino(Drink):
    def __init__(self):
        super().__init__("Капучіно", 50)
    
    def get_recipe(self) -> Dict[str, int]:
        return {"Кава": 20, "Вода": 30, "Молоко": 100}


class Latte(Drink):
    def __init__(self):
        super().__init__("Лате", 55)
    
    def get_recipe(self) -> Dict[str, int]:
        return {"Кава": 20, "Вода": 30, "Молоко": 150}


class Mocha(Drink):
    def __init__(self):
        super().__init__("Мокка", 60)
    
    def get_recipe(self) -> Dict[str, int]:
        return {"Кава": 20, "Вода": 30, "Молоко": 100, "Шоколад": 15}
