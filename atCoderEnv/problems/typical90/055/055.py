from sys import stdin

N, P, Q = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())

count = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            for l in range(k):
                for m in range(l):
                    # 大きな数の計算にならないように % P を散りばめている
                    if A[i] * A[j] % P * A[k] % P * A[l] % P * A[m] % P == Q:
                        count += 1


print(count)
