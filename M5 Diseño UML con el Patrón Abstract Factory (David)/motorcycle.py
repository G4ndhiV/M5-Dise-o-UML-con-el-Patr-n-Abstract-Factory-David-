from abc import ABC, abstractmethod

class Motorcycle(ABC):
    @abstractmethod
    def specifications(self) -> str:
        pass

    @abstractmethod
    def special_feature(self) -> str:
        pass

class ToyotaMotorcycle(Motorcycle):
    def specifications(self) -> str:
        return "Toyota 150cc - Moto urbana, 150cc, 15HP"

    def special_feature(self) -> str:
        return "Casco de seguridad incluido con la compra."

class BMWMotorcycle(Motorcycle):
    def specifications(self) -> str:
        return "BMW S1000RR - Moto deportiva, 999cc, 205HP"

    def special_feature(self) -> str:
        return "Sistema de frenos ABS avanzado."
