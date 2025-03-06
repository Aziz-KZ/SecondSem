X = int(input("Введите натуральное число X: "))

count = 0

for i in range(1, X + 1):
    if X % i == 0:
        count += 1

print("Количество делителей:", count)