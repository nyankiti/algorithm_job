from sys import stdin

N, K, X = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())

# 1ループ目を貪欲法で探索
for i in range(N):
    temp = A[i]
    q = temp // X
    # while q > 0 and K > 0:
    #     temp = temp - X
    #     q -= 1
    #     K -= 1
    # A[i] = temp
    # A[i] = A[i] - q*X
    # K -= q

    if K > q:
        A[i] = temp - q*X
        K -= q
    else:
        while q > 0 and K > 0:
            temp = temp - X
            q -= 1
            K -= 1
        A[i] = temp


A.sort(reverse=True)

# 余った中で最大限得する方法を探索
for i in range(N):
    temp = A[i]
    while temp > 0 and K > 0:
        temp -= X
        K -= 1
        if temp <= 0:
            temp = 0
            break
    A[i] = temp

print(sum(A))
