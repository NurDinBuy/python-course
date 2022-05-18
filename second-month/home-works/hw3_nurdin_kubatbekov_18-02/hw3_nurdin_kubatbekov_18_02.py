class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f'cpu + memory = {self.__cpu + self.__memory}'

    def __str__(self):
        return f'cpu: {self.__cpu}  memory: {self.__memory}'

    def __gt__(self, other):
        return f'{self.__cpu > self.__memory}'


class Phone:
    def __init__(self, sim_card_list):
        self.__sim_card_list = sim_card_list

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {number} с сим карты {simka}')

    def __str__(self):
        return f'sim card list: {self.__sim_card_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_card_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_card_list)

    def use_gps(self, location):
        return f'Проложен маршрут до {location}'

    def __str__(self):
        return f'cpu: {self.cpu}  memory: {self.memory}  sim card: {self.sim_card_list}'




number = input('Введите номер на который хотите позвонить: ')
sim_list = ['1 - O!', '2 - Beeline', '3 - Megacom']
simka = int(input(f'Выберите с какой сим карты будете звонить: {sim_list}'))
if simka == 1:
    simka = 'O!'
elif simka == 2:
    simka = 'Beeline'
elif simka == 3:
    simka = 'Megacom'
else:
    print('У вас нет такой сим карты!')


pc = Computer(4000, 10)
pc.make_computations()
phone = Phone(1)
smartPhone1 = SmartPhone(600, 16, sim_list[1])
smartPhone2 = SmartPhone(800, 8, sim_list[2])
smartPhone3 = SmartPhone(900, 32, sim_list[0])
smartPhone1.call('+996 709 813 738', sim_list[0])
smartPhone1.use_gps('Ысык-Кол')

print(pc)
print(pc.make_computations())
print(phone)
print(smartPhone1)
print(smartPhone2)
print(smartPhone3)
print(pc > smartPhone1)