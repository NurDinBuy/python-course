class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Animal:
    def __init__(self, name, age, address):
        self.__created()
        self.__name = name
        self.__age = age
        self.__address = address

    def __created(self):
        print("New animal was born")

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a number bigger than 0")
        else:
            self.__age = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def info(self):
        return f'Name: {self.__name} Age: {self.__age} ' \
               f'Adress: {self.get_address().city} {self.get_address().street} {self.get_address().number}'

    def get_address(self):
        return self.__address

    def set_address(self, value):
        if not isinstance(value, Address):
            raise ValueError("Value for address field must be 'Address' data type")
        else:
            self.__address = value

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, commands, address):
        super().__init__(name, age, address)
        self.__commands = commands

    @property
    def commands(self):
        print('Getter of commands field')
        return self.__commands

    @commands.setter
    def commands(self, value):
        print('Setter of commands field')
        self.__commands = value

    def info(self):
        return super().info() + f' Commands: {self.__commands}'

    def speak(self):
        print('Woooofff')


class Cat(Animal):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)

    def speak(self):
        print('Meuw')


class Fish(Animal):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)


dog = Dog("Snoopy", 2, "Sit", Address("Bishkek", "Ibraimova", 113))
print(dog.info())
cat = Cat("Tom", 4, Address("LA", "41 Avenue", 78))
print(cat.info())
dog.set_age(4)
dog.commands = "Sit, Run"
print(dog.info())
print(dog.commands)
# dog.created()
# cat.set_address("LA, New Street 89")
print(cat.info())
address_of_fish = Address("NY", "Wall Street", 675)
fish = Fish("Nemo", 5, address_of_fish)

animals_list = [fish, dog, cat]
for animal in animals_list:
    animal.speak()
