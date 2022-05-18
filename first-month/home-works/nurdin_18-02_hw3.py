data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

del numbers[0]
letters.append(numbers.pop(0))
numbers.insert(1, 2)
numbers.sort()

letters.reverse()
letters[1] = 'G'
letters[7] = 'c'

numbers = 1 ** 2, 2 ** 2, 3 ** 2

print(tuple(letters))
print(tuple(numbers))