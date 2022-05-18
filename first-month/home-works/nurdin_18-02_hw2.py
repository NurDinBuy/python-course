# УГАДАЙ ЧИСЛО
# minNum = 1
# maxNum = 100
#
# while True:
#     current = (minNum + maxNum) // 2
#     is_right = input('Ваше число:{}?(да, больше, меньше)'.format(current))
#     if is_right.lower() == 'да':
#         print('Я его угадал!')
#         break
#     elif is_right == 'больше':
#         minNum = current + 1
#     else:
#         maxNum = current - 1

# ГЛАСНЫЕ & СОГЛАСНЫЕ

while True:
    word = input("Введите любое Слово: ")
    if word == "EXIT":
        break
    print("Количество букв", len(word))
    gla = 0
    sog = 0
    for i in word:
        letter = i.lower()
        if letter == "a" or letter == "e" or letter == "а" or letter == "У" or letter == "о" or \
           letter == "i" or letter == "o" or letter == "ы" or letter == "э" or letter == "я" or \
           letter == "u" or letter == "y" or letter == "ю" or letter == "е" or letter == "ё" or \
           letter == "и":
            gla += 1

        else:
            sog += 1
    print("Гласные %i\n""Согласные %i" % (gla, sog))
    print(f'Гласные = {round(gla / len(word) * 100, 2)}%', f'Согласные = {round(sog / len(word) * 100, 2)}%')