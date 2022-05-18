# import random
# print(random.randint(1, 10))
# from random import randint, sample, choice, randrange
# students = ['edil', 'nurdin', 'erbol', 'ajar', 'ilyas', 'edil']
#
# while True:
#     player = randint(1, 6), randint(1, 6)
#     comp = randint(1, 6), randint(1, 6)
#
#     if sum(player) > sum(comp):
#         print('you win')
#         if sum(player) == 12:
#             print('bingo!')
#
#     elif sum(player) < sum(comp):
#         print('you lost')
#
#     else:
#         print('draw')
#
#     print(f'У вас выпало: {player}')
#     print(f'У опонента: {comp}')

# data = ['камень', 'ножницы', 'бумага']
#
# player = input('Выберите:\n '
#                '1) Камень\n'
#                '2) Ножницы\n'
#                '3) Бумага\n')
#
# comp = choice(data)
#
# print(f'NurDin {data[int(player)-1]} VS {comp} LOH')
#
# if player == '1' and comp == data[1] or player == '2' and comp == data[2]:
#     print('Ты выиграл')
# elif player == '1' and comp == data[2]:
#     print('YOU LOST')
# elif player == '1' and comp == data[0]:
#     print('DRAW')


# print(randint(1, 10))
# print(randrange(1, 10))

# print(choice(students))
# print(sample(students, 2))


# def greeting(name, greet_type='Привет'):
#     print(greet_type.title(), name.title())


# greeting('nurik', 'good morning')