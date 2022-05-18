

names = ['jack', 'sam', 'kate', 'steve', 'sam']
names1 = ['ali', 'said', 'umar', 'bakr', 'bakr']


def frequently(obj):
    c = 0
    most_f = None
    for i in obj:
        if obj.count(i) > c:
            c += 1
            most_f = i
            print(most_f)
    return most_f

print(frequently(names))
print(frequently(names1))




# word = 'python'
# word = word.title()
#
# print(word)
#
# def our_title(string: str):
#     changed = string[0].upper()
#     changed += string[1:]
#     return changed
#
# print(our_title('geektech'))


# def plus(a, b):
#     return a + b
#
# print(plus(2, 4))


# numbers = [0, 1, 2, 3,]

# def new(obj):
#     return obj ** 2

# def square_numbers(obj):
#     for i in obj:
#         print(new(i))

# print(square_numbers(numbers))



# lst = [1, 2, 3, 4]

# print(lst.pop(0))


# def menu(first, second, dessert, drink='чай',):
#     return {
#         'first': first,
#         'second': second,
#         'drink': drink,
#         'dessert': dessert
#     }
#
# lunch = menu('борщ', 'котлеты', 'брауни')
# dinner = menu('фанта', "мороженое", "каша", "омлет")
# dinner1 = menu(drink='фанта', dessert="мороженое", first="каша", second="омлет")
#
# print(dinner)
# print(dinner1)
# print(lunch)

# def get_total_price(length, width, price=200):
#     return length * width * price
#
# hall = get_total_price(5, 8, 200)
# kitchen = get_total_price(100, 3, 4)
# print(kitchen)


# def get_ploshad(length, width):
#     return length * width
#
# square_hall = get_ploshad(4, 7)
# square_kitchen = get_ploshad(3, 5)
#
# def get_price(square, price):
#     return square * price
#
# print(get_price(square_hall, 200))
# print(get_price(square_kitchen, 120))
#
# print('total: ', get_price(square_hall, 200) + get_price(square_kitchen, 120))


# a = 5
# b = 7
# s = a * b
# print(s, 'зал')
#
# price = 150
#
# result = s * price
# print(result)
#
# a = 4
# b = 3
# s = a * b
# print(s, 'кухня')
#
# price = 120
#
# result = s * price
# print(result)