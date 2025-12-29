from interfaces import IStorage
from typing import Dict


class Storage(IStorage):
    def __init__(self):
        self.ingredients: Dict[str, int] = {}
    
    def add_ingredient(self, ingredient_name: str, quantity: int) -> None:
        if ingredient_name in self.ingredients:
            self.ingredients[ingredient_name] += quantity
        else:
            self.ingredients[ingredient_name] = quantity
    
    def remove_ingredient(self, ingredient_name: str, quantity: int) -> bool:
        if ingredient_name not in self.ingredients:
            return False
        if self.ingredients[ingredient_name] < quantity:
            return False
        self.ingredients[ingredient_name] -= quantity
        return True
    
    def get_quantity(self, ingredient_name: str) -> int:
        return self.ingredients.get(ingredient_name, 0)
    
    def has_ingredients(self, recipe: Dict[str, int]) -> bool:
        for ingredient_name, quantity in recipe.items():
            if self.get_quantity(ingredient_name) < quantity:
                return False
        return True
    
    def get_all_ingredients(self) -> Dict[str, int]:
        return self.ingredients.copy()
    
    def set_ingredients(self, ingredients: Dict[str, int]) -> None:
        self.ingredients = ingredients.copy()
