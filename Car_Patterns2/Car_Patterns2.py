from abc import ABC, abstractmethod

# Фабричный паттерн
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Sedan(Car):
    def drive(self):
        return "Водим седан"

class SUV(Car):
    def drive(self):
        return "Водим Сув"

def get_car(car="Седан"):
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
        print("Обычный режим: " + car.drive())

class SportDriveStrategy(DriveStrategy):
    def drive(self, car):
        print("Режим спорткара: " + car.drive())

s0 = CarDriver("Сув", SportDriveStrategy())
s1 = CarDriver("Седан", NormalDriveStrategy())

