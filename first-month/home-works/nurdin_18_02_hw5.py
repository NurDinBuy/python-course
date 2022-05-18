# №1 Написать функцию, которая возвращает первое слово из полученного предложения.

# word = input('Введите предложение: ')
# def firstWord(word):
#    return word.split()[0]
# print(firstWord(word='Hello Word'))

# №2 Написать функцию, которая принимает неограниченное количество чисел и возвращает их среднее арифметическое.

# def hummer():
#     nums = []
#     while True:
#         numbers = int(input('Введите число: '))
#         nums.append(numbers)
#         print(nums)
#         if numbers == 0:
#             result = sum(nums) // len(nums)
#             print(result)
#             break
# hummer()

# №3 Написать функцию, проверяющую надежность пароля.

# while True:
#     password = input('Введите пароль и проверьте её надежность: ')
#     if password == 'q':
#         print('Программа завершена...')
#         break
#     def checkPass(password):
#         if len(password) >= 6:
#             if password.isdigit():
#                 print(False, 'Добавьте в папроль символы')
#             elif password.isalpha():
#                 print(False, 'Добавьте в папроль цифры')
#             else:
#                 print('Надежный папроль!')
#         else:
#             print(False, 'Не надженый пароль')
#     checkPass(password)

