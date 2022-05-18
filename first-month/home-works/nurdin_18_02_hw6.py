# Создать/сгенерировать список ten, состоящий из целых чисел от 1 до 10

ten = [i for i in range(1, 11)]
print(ten)

# Создать список evens, который состоит из четных чисел списка ten

evens = list(filter(lambda x: x % 2 == 0, ten))
print(evens)

# for i in ten:
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)

# Вывести на экран список возведенных в квадрат чисел от списка evens.

square = list(map(lambda x: x ** 2, evens))
print(square)

# square = [i ** 2 for i in evens]
# print(square)

# Создать функцию для вывода объекта списка по указанному индексу.

def indexing(hola = ten):
    while True:
        try:
            ind = input('Введите индекс: ')
            if ind == 'exit':
                print('Программа завершена!')
                break
            else:
                print(hola[int(ind)])
        except Exception:
            print(f'Вы можете ввести индекс только от 0 до {len(ten)-1}')
indexing(ten)