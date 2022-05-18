# file = open('data.txt', 'w')
# file.write('Kotok bash')
# file.close()
from time import sleep
#
#
#
# with open('data.txt', 'a') as file:
#     file.write('\nSalam')
#
# with open('data.txt', 'r', encoding='UTF-8') as file:
#     for i in file.read():
#         print(i, end='')
#         sleep(0.09)

from random import randint, choice, sample

students = [3, 4, 5, 10, 11]
data = []
materials = list(range(1, 9))
while True:
    print(students)
    id_s = choice(students)
    name = input(f'name for {id_s}').title()
    print(sample(materials, 3))
    rate = int(input(f'rate for {name}: '))
    with open('data.txt', 'a') as file:
        file.write(f'id:{id_s}, name: {name}, rate: {rate}')
    students.remove(id_s)
