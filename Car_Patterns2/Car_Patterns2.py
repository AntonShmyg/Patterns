from abc import ABC, abstractmethod

# Фабричный паттерн
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Sedan(Car):
    def drive(self):
        return "Driving sedan"

class SUV(Car):
    def drive(self):
        return "Driving SUV"

def get_car(car="sedan"):
    cars = dict(sedan=Sedan(), suv=SUV())
    return cars[car]

# Фасад
class CarFacade:
    def __init__(self, car_type):
        self._car = get_car(car_type)

    def drive(self):
        self._car.drive()

# Стратегия
class CarDriver:
    def __init__(self, car_type, drive_strategy):
        self._car = CarFacade(car_type)
        self._strategy = drive_strategy

    def execute(self):
        self._strategy.drive(self._car)

class DriveStrategy:
    @abstractmethod
    def drive(self, car):
        pass

class NormalDriveStrategy(DriveStrategy):
    def drive(self, car):
        print("Driving normally: " + car.drive())

class SportDriveStrategy(DriveStrategy):
    def drive(self, car):
        print("Driving sportily: " + car.drive())

s0 = CarDriver("suv", SportDriveStrategy())
s1 = CarDriver("sedan", NormalDriveStrategy())

s0.execute()
s1.execute()

