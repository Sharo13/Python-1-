class Car:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    def set_brand(self, brand):
        if not isinstance(brand, str):
            raise ValueError("Brand must be a string")
        self._brand = brand

    def get_brand(self):
        return self._brand

    def set_model(self, model):
        if not isinstance(model, str):
            raise ValueError("Model must be a string")
        self._model = model

    def get_model(self):
        return self._model

    def set_year(self, year):
        if not isinstance(year, int):
            raise ValueError("Year must be an integer")
        self._year = year

    def get_year(self):
        return self._year

car = Car("Toyota", "Camry", 2022)
print(car.get_brand())  # Output: Toyota
print(car.get_model())  # Output: Camry
print(car.get_year())   # Output: 2022

car.set_brand("Honda")
car.set_model("Accord")
car.set_year(2023)

print(car.get_brand())  # Output: Honda
print(car.get_model())  # Output: Accord
print(car.get_year())   # Output: 2023
