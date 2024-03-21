# Single Responsibility Principle
class BookDetails:
    def __init__(self, title, author):
        self.title = title
        self.author = author 

class BookPricing:
    def __init__(self, price):
        self.price = price 

    def get_discount_price(self, discount):
        return self.price * (1 - discount) 



# Open/Closed Principle
from abc import ABC, abstractmethod

class Payment(ABC):
    """ გადახდის კლასი გადახდების დასამუშავებლად
    """
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    """
    გადახდის კლასი საკრედიტო ბარათით გადახდების დასამუშავებლად
    """
    def process_payment(self, amount):
        pass

class PayPalPayment(Payment):
    """
    გადახდის კლასი PayPalით გადახდების დასამუშავებლად 
    """
    def process_payment(self, amount):
        pass



# Liskov Substitution Principle
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fuel_capacity(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):
    def fuel_capacity(self):
        return 100

    def fuel_type(self):
        return "Gasoline"

class ElectricCar(Vehicle):
    def fuel_capacity(self):
        return 100

    def fuel_type(self):
        return "Battery"



# Interface Segregation Principle
from abc import ABC, abstractmethod

class AudioPlayer(ABC):
    @abstractmethod
    def play_audio(self):
        pass

class VideoPlayer(ABC):
    @abstractmethod
    def play_video(self):
        pass

class AllMediaPlayer(AudioPlayer, VideoPlayer):
    pass

class AudioOnlyPlayer(AudioPlayer):
    pass

class VideoOnlyPlayer(VideoPlayer):
    pass


# Dependency Inversion Principle (DIP)
from abc import ABC, abstractmethod 

class Display(ABC):
    @abstractmethod
    def show(self, data):
        pass 

class ConsoleDisplay(Display):
    def show(self, data):
        print(data) 

class WeatherStation:
    def report(self, display):
        display.show("Weather Data") 
