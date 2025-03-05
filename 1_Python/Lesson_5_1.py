number = int(input("Целое число: "))
if number == 0:
    print("Нулевое число")
elif number > 0:
    if number % 2 == 0:
        print("Положительное четное число")
    else:
        print("Положительное нечетное число")
else:
    if number % 2 == 0:
        print("Отрицательное четное число")
    else:
        print("Отрицательное нечетное число")
if number % 2 != 0:
    print("Число не является четным")
