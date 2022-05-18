class Person:
    def __init__(self , age, name):
        self.__age = age
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return f'{self.__name} {self.__age}'
