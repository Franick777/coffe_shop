from interfaces import IBarista, IOrder, IStorage
from drink import Drink


class Barista(IBarista):
    def __init__(self, name: str, storage: IStorage):
        self.name = name
        self.storage = storage
    
    def prepare_drink(self, order: IOrder) -> bool:
        drink = order.get_drink()
        recipe = drink.get_recipe()
        
        if not self.storage.has_ingredients(recipe):
            print(f"  {self.name}: Недостатньо інгредієнтів для {drink.name}")
            return False
        
        for ingredient_name, quantity in recipe.items():
            self.storage.remove_ingredient(ingredient_name, quantity)
        
        print(f"  {self.name}: Приготував {drink.name}")
        return True
