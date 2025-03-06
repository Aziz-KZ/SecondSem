N = int(input())

Ai = list(map(int, input().split()))

if N > 1:
   Ai = [Ai[-1]] + Ai[:-1]

print(*Ai)