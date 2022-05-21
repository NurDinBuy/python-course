class MusicPlayable:
    def playMusic(self, song):
        pass


class Car(MusicPlayable):
    '''Car class is used for creting object of car'''

    def __init__(self, year, model):
        self.__year = year
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    def drive(self):
        print('I am driving')

    def __str__(self):
        return f'Model: {self.__model} Year: {self.__year}'

    def playMusic(self, song):
        print("Now in the car is playing " + song)

    def __eq__(self, other):
        return self.__year == other.__year

    def __del__(self):
        print(f'{self.__model} deleted from memory')


class ElectricCar(Car):
    def __init__(self, year, model, battery):
        Car.__init__(self, year, model)
        self.__battery = battery

    def __str__(self):
        return super(ElectricCar, self).__str__() + f' Battery: {self.__battery}'

    def drive(self):
        print('I am driving by electricity')


class FuelCar(Car):
    __total_fuel = 500

    @staticmethod
    def fuel_type():
        print("AI-98")

    @classmethod
    def get_total_fuel(cls):
        return cls.__total_fuel

    def __init__(self, year, model, fuel_bank):
        Car.__init__(self, year, model)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= fuel_bank

    def __str__(self):
        return super(FuelCar, self).__str__() + f' Fuel bank: {self.__fuel_bank}'

    def drive(self):
        print('I am driving by fuel')

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, year, model, battery, fuel_bank):
        ElectricCar.__init__(self, year, model, battery)
        FuelCar.__init__(self, year, model, fuel_bank)


class SmartPhone(MusicPlayable):
    def playMusic(self, song):
        print('Now smartphone is playing ' + song)


my_car = Car(2020, "Honda Fit")
print(my_car)
my_car.drive()

tesla_car = ElectricCar(2022, "Model X", 25000)
print(tesla_car)
tesla_car.drive()

toyota_car = FuelCar(2022, "Toyota Camry", 65)
print(toyota_car)
toyota_car.drive()

prius_car = HybridCar(2021, "Toyota Prius", 30000, 45)
print(prius_car)
prius_car.drive()

print(Car.__doc__)

print(HybridCar.__mro__)

android_phone = SmartPhone()

obj_list = [android_phone, my_car, tesla_car, toyota_car, prius_car]

for obj in obj_list:
    obj.playMusic("Billy jean")

print(toyota_car + prius_car)
print(toyota_car == tesla_car)

print(FuelCar.get_total_fuel())
FuelCar.fuel_type()
