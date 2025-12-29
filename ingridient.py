from abc import ABC, abstractmethod


class Ingredient(ABC):
    def __init__(self, name: str, unit: str):
        self.name = name
        self.unit = unit
    
    @abstractmethod
    def get_price_per_unit(self) -> float:
        pass


class Coffee(Ingredient):
    def __init__(self):
        super().__init__("Кава", "г")
    
    def get_price_per_unit(self) -> float:
        return 0.5


class Milk(Ingredient):
    def __init__(self):
        super().__init__("Молоко", "мл")
    
    def get_price_per_unit(self) -> float:
        return 0.03


class Sugar(Ingredient):
    def __init__(self):
        super().__init__("Цукор", "г")
    
    def get_price_per_unit(self) -> float:
        return 0.02


class Water(Ingredient):
    def __init__(self):
        super().__init__("Вода", "мл")
    
    def get_price_per_unit(self) -> float:
        return 0.01


class Chocolate(Ingredient):
    def __init__(self):
        super().__init__("Шоколад", "г")
    
    def get_price_per_unit(self) -> float:
        return 0.8
