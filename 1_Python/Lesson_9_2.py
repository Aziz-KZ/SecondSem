count1 = int(input())
list1 = []
for _ in range(count1):
    number = input()
    list1.append(number)

set1 = set(list1)

count2 = int(input())
list2 = []
for _ in range(count2):
    number = input()
    list2.append(number)

set2 = set(list2)

print("Количество общих элементов:", len(set1.intersection(set2)))
