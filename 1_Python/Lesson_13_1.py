import random

def pl(t):
    for i in t:
        print(*i)

x = int(input("Введите количество строк: "))
y = int(input("Введите количество столбцов: "))

matrix_1 = [[random.randint(-100, 100) for _ in range(y)] for _ in range(x)]
matrix_2 = [[random.randint(-100, 100) for _ in range(y)] for _ in range(x)]

matrix_3 = [[matrix_1[i][j] + matrix_2[i][j] for j in range(y)] for i in range(x)]

print("Первая матрица:")
pl(matrix_1)

print("\nВторая матрица:")
pl(matrix_2)

print("\nРезультирующая матрица после сложения:")
pl(matrix_3)