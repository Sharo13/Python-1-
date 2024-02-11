from datetime import datetime

class Car:
    number_of_cars = 0
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.number_of_cars += 1

    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

    def age_of_car(self):
        current_year = datetime.now().year
        age = current_year - self.year
        print(f"{self.brand} {self.model} is {age} years old.")
    @classmethod
    def total_cars(cls):
        return cls.number_of_cars
    
class ElectricCar (Car):
    def __init__(self, brand, model, year, battery_life) :
        super().__init__(brand, model, year)
        self.battery_life = battery_life
    def battery_info(self):
        print(f"The battery life of this machine is {self.battery_life} hours")


"""RUN PROGRAM"""

car1 = Car("Toyota", "Camry", 2019)
car2 = Car("Honda", "Accord", 2020)
car3 = Car("Porsche", "Boxster", 2023)

car3.car_info()
car3.age_of_car()

electric_car = ElectricCar("Tesla", "Model S", 2022, 300)
electric_car.battery_info()
        
print("Total number of cars:", Car.total_cars())