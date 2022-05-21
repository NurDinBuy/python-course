class Transport:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def change_color(self, new_color):
        self.color = new_color
        print(f'Rocket {self.model} changed color to {self.color}')


class Car(Transport):
    wheels = 4

    def __init__(self, model, year, color, penalties=0.0):
        super().__init__(model, year, color)
        self.penalties = penalties

    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Rocket(Transport):
    def __init__(self, model, year, color):
        Transport.__init__(self, model, year, color)


class Truck(Car):
    wheels = 10

    def __init__(self, model, year, color, penalties, load_capacity):
        super().__init__(model, year, color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, weight, product):
        print(f'{self.model} loaded cargo with {product} {weight} kg ')


print(f'We need to buy {20 * Car.wheels * 3000} som')


mazda_car = Car('Mazda Demio', 2001, 'Red')
print(f'Model: {mazda_car.model} Year: {mazda_car.year} Color: {mazda_car.color}'
      f'Penalties: {mazda_car.penalties}')
mazda_car.color = 'Black'
print(f'Model: {mazda_car.model} Year: {mazda_car.year} Color: {mazda_car.color}'
      f'Penalties: {mazda_car.penalties}')
mazda_car.drive('Osh')


# БЫ - ЫМ - ВЫ
bmw_car = Car(model='BMW X5', year=2018, color='Silver', penalties=2000)

print(f'Model: {bmw_car.model} Year: {bmw_car.year} Color: {bmw_car.color} '
      f'Penalties: {bmw_car.penalties} Wheels: {bmw_car.wheels}')

bmw_car.drive('New York')
bmw_car.change_color('White')

porsche_car = Car('Porsche Cayenne', 2020, 'Yellow', 1100)

bmw_car.wheels = 6
Car.wheels = 6

audi_car = Car('Audi 100', 2019, 'Blue')
print(f'Model: {audi_car.model} Year: {audi_car.year} Color: {audi_car.color} '
      f'Penalties: {audi_car.penalties} Wheels: {audi_car.wheels}')

falcon_rocket = Rocket('Falcon 9', 2022, 'White')
print(f'Model: {falcon_rocket.model} Year: {falcon_rocket.year} Color: {falcon_rocket.color} ')
falcon_rocket.change_color('Blue')

man_truck = Truck('Man 900', 2000, 'Green', 0.0, 2000)
print(f'Model: {man_truck.model} Year: {man_truck.year} Color: {man_truck.color} '
      f'Penalties: {man_truck.penalties} Wheels: {man_truck.wheels}'
      f'Load Capacity: {man_truck.load_capacity}')