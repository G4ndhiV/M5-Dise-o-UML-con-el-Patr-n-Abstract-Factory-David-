from factory import ToyotaFactory, BMWFactory

if __name__ == "__main__":
    toyota_factory = ToyotaFactory()
    toyota_car = toyota_factory.create_car()
    toyota_motorcycle = toyota_factory.create_motorcycle()

    print("Toyota Factory:")
    print(toyota_car.specifications())
    print(toyota_car.special_feature())
    print(toyota_motorcycle.specifications())
    print(toyota_motorcycle.special_feature())

    bmw_factory = BMWFactory()
    bmw_car = bmw_factory.create_car()
    bmw_motorcycle = bmw_factory.create_motorcycle()

    print("\nBMW Factory:")
    print(bmw_car.specifications())
    print(bmw_car.special_feature())
    print(bmw_motorcycle.specifications())
    print(bmw_motorcycle.special_feature())
