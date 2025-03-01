from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def specifications(self) -> str:
        pass

    @abstractmethod
    def special_feature(self) -> str:
        pass

class ToyotaCar(Car):
    def specifications(self) -> str:
        return "Toyota Corolla - Sedán, 1.8L, 139HP"

    def special_feature(self) -> str:
        return "Garantía de 3 años incluida."

class BMWCar(Car):
    def specifications(self) -> str:
        return "BMW M3 - Deportivo, 3.0L, 473HP"

    def special_feature(self) -> str:
        return "Incluye paquete de mantenimiento premium."
