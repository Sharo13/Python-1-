import pytest

class Vehicle:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
    self.gaz_tank_size = 45
    self.fuel_level = 0
  

  @property
  def fuel_up(self):
    self.fuel_level = self.gaz_tank_size

    if self.fuel_level:
      return "Gas tank is now full or can move."
    
    return "Gas tank is empty and can not move."
  

  @property
  def drive(self):
    return f"The {self.model} is now driving."


class ElectricVehicle(Vehicle):
  def __init__(self, brand, model, year):
    super().__init__(brand, model, year)

    self.battery_size = 85
    self.charge_level = 0
  

  @property
  def charge(self):
    self.charge_level = 100

    return "The vehicle is now charged."
  

  @property
  def fuel_up(self):
    return "This vehicle has no fuel tank!"
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def test_vehicle_init():
  car = Vehicle("Porsche", "Taycan GTS", 2022)
  assert car.brand == "Porsche"
  assert car.model == "Taycan GTS"
  assert car.year == 2022
  assert car.gaz_tank_size == 45
  assert car.fuel_level == 0

def test_vehicle_fuel_up_empty():
  car = Vehicle("Porsche", "Taycan GTS", 2022)
  assert car.fuel_up == "Gas tank is empty!"

def test_vehicle_fuel_up_full():
  car = Vehicle("Porsche", "Taycan GTS", 2022)
  car.fuel_level = car.gaz_tank_size
  assert car.fuel_up == "Gas tank is now full!"

def test_vehicle_drive():
   car = Vehicle("Porsche", "Taycan GTS", 2022)
   assert car.drive == "Porsche is now driving."