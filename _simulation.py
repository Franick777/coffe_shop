import random
from container import DIContainer


class CafeSimulation:
    def __init__(self, container: DIContainer):
        self.container = container
        self.day = container.day
    
    def run(self):
        cafe = self.container.get_cafe()
        storage = self.container.get_storage()
        stat_saver = self.container.get_stat_saver()
        customer_generator = self.container.get_customer_generator()
        
        print(f"\n{'#'*60}")
        print(f"#{'ДЕНЬ ' + str(self.day):^58}#")
        print(f"{'#'*60}")
        
        cafe.open_day()
        
        if self.day == 1 or storage.get_quantity("Кава") < 100:
            cafe.buy_supplies()
        
        cafe.show_menu()
        
        num_customers = random.randint(8, 15)
        print(f"\nСьогодні очікується {num_customers} відвідувачів\n")
        
        for i in range(num_customers):
            customer = customer_generator.generate_customer()
            cafe.serve_customer(customer)
        
        if random.random() < 0.3 and cafe.get_balance() > 300:
            print("\nДодаткова закупівля інгредієнтів")
            cafe.buy_supplies()
        
        cafe.close_day()
        
        stat_saver.save_state(
            cafe.get_balance(),
            storage.get_all_ingredients(),
            self.day + 1
        )
        
        print("Дані збережено. Запустіть програму знову для наступного дня.")


if __name__ == "__main__":
    container = DIContainer()
    simulation = CafeSimulation(container)
    simulation.run()
    simulation.run()
