from sys import stdin

N, Q = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())

for _ in range(Q):
    x, k = map(int, stdin.readline().split())
    k_count = 0
    for i in range(N):
        if A[i] == x:
            if k_count+1 == k:
                result = i+1
                break
            else:
                k_count += 1
    else:
        result = -1
    print(result)
