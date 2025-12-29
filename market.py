from interfaces import IMarket
from typing import List
from ingridient import Ingredient, Coffee, Milk, Sugar, Water, Chocolate


class Market(IMarket):
    def __init__(self):
        self.available_ingredients = [
            Coffee(),
            Milk(),
            Sugar(),
            Water(),
            Chocolate()
        ]
    
    def buy_ingredient(self, ingredient_name: str, quantity: int) -> float:
        for ingredient in self.available_ingredients:
            if ingredient.name == ingredient_name:
                return ingredient.get_price_per_unit() * quantity
        return 0
    
    def get_available_ingredients(self) -> List[Ingredient]:
        return self.available_ingredients
