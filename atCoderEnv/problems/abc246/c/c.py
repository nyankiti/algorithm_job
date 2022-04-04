from sys import stdin

N, K, X = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())

# 1ループ目を貪欲法で探索
for i in range(N):
    temp = A[i]
    q = temp // X

    if K > q:
        A[i] = temp - q*X
        K -= q
    else:
        A[i] = temp - K*X
        K = 0

A.sort(reverse=True)
print(sum(A[K:]))
