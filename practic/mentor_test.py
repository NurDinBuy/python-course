while True:
    a = float(input("Введите первое число: "))
    b = (input("Введите операцию(+, -, *, /): "))
    c = float(input("Введите второе число: "))

    if b == "+":
        answer = a+c
    elif b == "-":
        answer = a-c
    elif b == "*":
        answer = a*c

    elif b == "/" and c == 0:
        print("Нельза делить на 0!")
    elif b == "/":
        answer = a/c

    else:
        print("Не опознанная операция")

    print(f"Вывод: {answer}")