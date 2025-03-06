N = int(input())
numbers = [int(input()) for _ in range(N)]

print(*numbers[::-1])