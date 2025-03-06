n = int(input("Введите количество чисел: "))

numbers = set(map(int, input("Введите числа через пробел: ").split()))

print("Количество различных чисел:", len(numbers))
