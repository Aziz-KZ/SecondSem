A = int(input("Введите A: "))
B = int(input("Введите B: "))

for number in range(A, B + 1):
    if number % 2 == 0:
        print(number, end=' ')