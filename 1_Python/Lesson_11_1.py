def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Введите натуральное число: "))

fact = factorial(num)

factorials_list = [factorial(i) for i in range(fact, 0, -1)]

print(f"Факториал числа {num} равен {fact}")
print("Список факториалов в убывающем порядке:", factorials_list)