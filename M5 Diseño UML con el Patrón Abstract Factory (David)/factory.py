from abc import ABC, abstractmethod
from car import Car, ToyotaCar, BMWCar
from motorcycle import Motorcycle, ToyotaMotorcycle, BMWMotorcycle

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self) -> Motorcycle:
        pass

class ToyotaFactory(VehicleFactory):
    def create_car(self) -> Car:
        return ToyotaCar()

    def create_motorcycle(self) -> Motorcycle:
        return ToyotaMotorcycle()

class BMWFactory(VehicleFactory):
    def create_car(self) -> Car:
        return BMWCar()

    def create_motorcycle(self) -> Motorcycle:
        return BMWMotorcycle()
