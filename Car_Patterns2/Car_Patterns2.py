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

# Фасад
class CarFacade:
    def __init__(self, car):
        self._car = car

    def drive(self):
        self._car.drive()

# Стратегия
class CarDriver:
    def __init__(self, car, drive_strategy):
        self._car = car
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

sedan = Sedan()
suv = SUV()

car1 = CarFacade(sedan)
car2 = CarFacade(suv)

strategy1 = NormalDriveStrategy()
strategy2 = SportDriveStrategy()

car_driver1 = CarDriver(car1, strategy1)
car_driver2 = CarDriver(car2, strategy2)

car_driver1.execute()
car_driver2.execute()