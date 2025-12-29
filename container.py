from storage import Storage
from market import Market
from barista import Barista
from cafe import Cafe
from customer import CustomerGenerator
from stat_saver import StatSaver
from interfaces import IStorage, IMarket, IBarista, ICafe, IStatSaver


class DIContainer:
    def __init__(self):
        self.stat_saver: IStatSaver = StatSaver()
        state = self.stat_saver.load_state()
        
        self.day = state["day"]
        self.balance = state["balance"]
        
        self.storage: IStorage = Storage()
        self.storage.set_ingredients(state["ingredients"])
        
        self.market: IMarket = Market()
        
        self.barista: IBarista = Barista("Олена", self.storage)
        
        self.cafe: ICafe = Cafe(
            "Кав'ярня 'Ранкова кава'",
            state["balance"],
            self.storage,
            self.market,
            self.barista
        )
        
        self.customer_generator = CustomerGenerator()
    
    def get_cafe(self) -> ICafe:
        return self.cafe
    
    def get_storage(self) -> IStorage:
        return self.storage
    
    def get_stat_saver(self) -> IStatSaver:
        return self.stat_saver
    
    def get_customer_generator(self) -> CustomerGenerator:
        return self.customer_generator
