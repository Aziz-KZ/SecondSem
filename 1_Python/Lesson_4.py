a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))

P = 2 * (a + b)
S = a * b

print("Периметр прямоугольника:", P)
print("Площадь прямоугольника:", S)


n = 46275
a, b, c, d, e = map(int, str(n))

result = (d ** e * c) / (a - b)
print(float(result))
