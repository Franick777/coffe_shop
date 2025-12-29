from interfaces import ICafe, IStorage, IMarket, IBarista, ICustomer
from typing import List
from order import Order
from drink import Espresso, Americano, Cappuccino, Latte, Mocha


class Cafe(ICafe):
    def __init__(self, name: str, balance: float, storage: IStorage, 
                 market: IMarket, barista: IBarista):
        self.name = name
        self.balance = balance
        self.storage = storage
        self.market = market
        self.barista = barista
        self.daily_revenue = 0
        self.daily_expenses = 0
        self.drinks_sold = 0
        self.menu = [Espresso(), Americano(), Cappuccino(), Latte(), Mocha()]
    
    def open_day(self) -> None:
        print(f"\n{'='*60}")
        print(f"{self.name} відчиняє двері!")
        print(f"Баланс: {self.balance:.2f} грн")
        print(f"{'='*60}\n")
        self.daily_revenue = 0
        self.daily_expenses = 0
        self.drinks_sold = 0
    
    def close_day(self) -> None:
        profit = self.daily_revenue - self.daily_expenses
        print(f"\n{'='*60}")
        print(f"{self.name} закривається")
        print(f"Статистика дня:")
        print(f"  • Продано напоїв: {self.drinks_sold}")
        print(f"  • Виручка: {self.daily_revenue:.2f} грн")
        print(f"  • Витрати: {self.daily_expenses:.2f} грн")
        print(f"  • Прибуток: {profit:.2f} грн")
        print(f"Залишок: {self.balance:.2f} грн")
        print(f"{'='*60}\n")
    
    def serve_customer(self, customer: ICustomer) -> None:
        print(f"\n{customer.get_name()} зайшов до кав'ярні")
        
        drink = customer.choose_drink()
        if drink is None:
            print(f"  {customer.get_name()} не має достатньо грошей і пішов")
            return
        
        print(f"  {customer.get_name()} замовив {drink.name} ({drink.price} грн)")
        
        order = Order(drink)
        
        if self.barista.prepare_drink(order):
            payment = customer.pay(drink.price)
            if payment > 0:
                self.balance += payment
                self.daily_revenue += payment
                self.drinks_sold += 1
                print(f"  {customer.get_name()} заплатив {payment:.2f} грн і пішов задоволений")
            else:
                print(f"  {customer.get_name()} не зміг заплатити")
        else:
            print(f"  {customer.get_name()} пішов без замовлення")
    
    def buy_supplies(self) -> None:
        print(f"\nЗакупівля інгредієнтів на ринку:")
        
        supplies = {
            "Кава": 500,
            "Молоко": 2000,
            "Вода": 3000,
            "Цукор": 500,
            "Шоколад": 200
        }
        
        total_cost = 0
        for ingredient_name, quantity in supplies.items():
            cost = self.market.buy_ingredient(ingredient_name, quantity)
            total_cost += cost
        
        if total_cost > self.balance:
            print(f"  Недостатньо коштів для закупівлі (потрібно {total_cost:.2f} грн)")
            return
        
        self.balance -= total_cost
        self.daily_expenses += total_cost
        
        for ingredient_name, quantity in supplies.items():
            self.storage.add_ingredient(ingredient_name, quantity)
            print(f"  Куплено {ingredient_name}: {quantity} за {self.market.buy_ingredient(ingredient_name, quantity):.2f} грн")
        
        print(f"  Загальна вартість: {total_cost:.2f} грн")
    
    def get_balance(self) -> float:
        return self.balance
    
    def set_balance(self, balance: float) -> None:
        self.balance = balance
    
    def show_menu(self) -> None:
        print("\nМеню:")
        for drink in self.menu:
            print(f"  • {drink.name}: {drink.price} грн")
