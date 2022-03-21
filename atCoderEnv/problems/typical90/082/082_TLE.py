from sys import stdin

mod = 10 ** 9 + 7
L, R = map(int, stdin.readline().split())


# 以下のように単純に書くとTLEする
for i in range(L, R+1):
    ans = (ans + len(str(i)) * i) % mod

print(ans)
