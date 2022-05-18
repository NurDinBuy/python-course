from random import randint
from datetime import datetime as dt
comp = randint(1, 100)
trys = 0
start = dt.now()
while True:
    try:
        player = int(input('Угадайте число от 1 до 100: '))
        if player > 100:
            print('Загаданное число только от 1 до 100')
        elif player < 1:
            print('Загаданное число положительное (от 1 до 100)')
        if player < comp:
            print('>')
            trys += 1
        elif player > comp:
            print('<')
            trys += 1
        else:
            print('Вы угадали!')
            res = dt.now() - start
            print(f'Попыток: {trys}\n'
                  f'Время игры: {res}')
            break
    except Exception:
        print('Вводите числа!')