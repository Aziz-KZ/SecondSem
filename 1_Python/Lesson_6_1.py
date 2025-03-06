n = int(input("Количество целых чисел: "))
count_zeros = 0

print(f"Количество {n} целых чисел:")
for _ in range(n):
    number = int(input())
    if number == 0:
        count_zeros += 1

print("Равны нулю:", count_zeros)

