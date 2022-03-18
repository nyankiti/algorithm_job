from sys import stdin

N = int(stdin.readline())

mod = 10**9+7
ans = 1

for i in range(N):
    ans = (ans * sum(map(int, stdin.readline().split()))) % mod
print(ans)
