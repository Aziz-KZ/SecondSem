n = int(input())
m = int(input())

weight = []
for _ in range(n):
    weight.append(int(input()))

boats = 0
used = [False] * n

for i in range(n):
    if used[i]:
        continue
    boats += 1
    for j in range(i + 1, n):
        if not used[j] and weight[i] + weight[j] <= m:
            used[j] = True
            break
    used[i] = True

print("Необходимое количество лодок:", boats)