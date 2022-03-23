from sys import stdin

N, X, Y = map(int, stdin.readline().split())


count = 0
for i in range(1, N+1):
    if i % X == 0 or i % Y == 0:
        count += 1
print(count)
