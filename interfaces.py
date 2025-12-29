from abc import ABC, abstractmethod
from typing import Dict


class IStorage(ABC):
    @abstractmethod
    def add_ingredient(self, ingredient_name: str, quantity: int) -> None:
        pass
    
    @abstractmethod
    def remove_ingredient(self, ingredient_name: str, quantity: int) -> bool:
        pass
    
    @abstractmethod
    def get_quantity(self, ingredient_name: str) -> int:
        pass
    
    @abstractmethod
    def has_ingredients(self, recipe: Dict[str, int]) -> bool:
        pass
    
    @abstractmethod
    def get_all_ingredients(self) -> Dict[str, int]:
        pass


class IMarket(ABC):
    @abstractmethod
    def buy_ingredient(self, ingredient_name: str, quantity: int) -> float:
        pass


class IBarista(ABC):
    @abstractmethod
    def prepare_drink(self, order) -> bool:
        pass


class IOrder(ABC):
    @abstractmethod
    def get_drink(self):
        pass
    
    @abstractmethod
    def get_total_price(self) -> float:
        pass


class ICustomer(ABC):
    @abstractmethod
    def choose_drink(self):
        pass
    
    @abstractmethod
    def pay(self, amount: float) -> float:
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        pass


class ICafe(ABC):
    @abstractmethod
    def open_day(self) -> None:
        pass
    
    @abstractmethod
    def close_day(self) -> None:
        pass
    
    @abstractmethod
    def serve_customer(self, customer: ICustomer) -> None:
        pass
    
    @abstractmethod
    def buy_supplies(self) -> None:
        pass


class IStatSaver(ABC):
    @abstractmethod
    def save_state(self, balance: float, ingredients: Dict[str, int], day: int) -> None:
        pass
    
    @abstractmethod
    def load_state(self) -> Dict:
        pass
