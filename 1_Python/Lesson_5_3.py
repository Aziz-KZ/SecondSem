x = int(input("Минимальная сумма инвестиций: "))
a = int(input("Сколько долларов у Майкла: "))
b = int(input("Сколько долларов у Ивана: "))

if a >= x and b >= x:
    print(2)
elif a >= x:
    print("Mike")
elif b >= x:
    print("Ivan")
elif a + b >= x:
    print(1)
else:
    print(0)