from sys import stdin


N, K = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())
*B, = map(int, stdin.readline().split())

dp_A = [False]*N
dp_B = [False]*N

dp_A[0] = True
dp_B[0] = True

for i in range(N-1):
    if dp_A[i]:
        dp_A[i+1] = dp_A[i+1] or abs(A[i] - A[i+1]) <= K
        dp_B[i+1] = dp_B[i+1] or abs(A[i] - B[i+1]) <= K
    if dp_B[i]:
        dp_A[i+1] = dp_A[i+1] or abs(B[i] - A[i+1]) <= K
        dp_B[i+1] = dp_B[i+1] or abs(B[i] - B[i+1]) <= K

if dp_A[-1] or dp_B[-1]:
    print("Yes")
else:
    print("No")
