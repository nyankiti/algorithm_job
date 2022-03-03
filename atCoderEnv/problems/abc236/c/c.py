from sys import stdin

N, M = map(int, stdin.readline().split())
*S, = input().split()
*T, = input().split()

i = 0
j = 0
while i < N:
    if S[i] == T[j]:
        print("Yes")
        i += 1
        j += 1
    else:
        print("No")
        i += 1
