from random import randint
import time

name = input('Ваше имя?: ')
trys = int(input('Сколько попыток вам дать?: '))
show = trys
game_time = time.time()
while trys != 0:
    trys -= 1
    a = randint(1, 9)
    b = randint(1, 9)
    gamer = int(input(f'{a} * {b} = ?: '))
    right_answer = a * b

    if gamer == right_answer:
        print(f'Правильно! \n'
              f'Ответ - {right_answer}')
        with open('result.txt', 'a', encoding='UTF=8') as file:
            file.write(f'{a} * {b} = {right_answer}  ({right_answer}) Правильно\n')
    else:
        print(f'Непрвильно! \n'
              f'Ответ - {right_answer}')
        with open('result.txt', 'a', encoding='UTF=8') as file:
            file.write(f'{a} * {b} = {right_answer}  ({right_answer}) Неправильно\n')
        print(f'Осталось попыток {trys}\n')

print(f'Имя: {name}\n'
      f'Попыток: {show}\n'
      f'Время: {round(time.time() - game_time)} секунд\n')
with open('result.txt', 'a', encoding='UTF=8') as file:
    file.write(f'Имя: {name}\n'
               f'Попыток: {show}\n'
               f'Время: {round(time.time() - game_time)} секунд\n')