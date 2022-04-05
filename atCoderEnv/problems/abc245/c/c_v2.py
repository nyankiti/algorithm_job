from sys import stdin, exit

N, K = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())
*B, = map(int, stdin.readline().split())

X = []
X.append(A[0])
for i in range(1, N-1):
    if abs(X[i-1] - A[i]) <= K and (abs(A[i] - A[i+1]) <= K or abs(A[i] - B[i+1]) <= K):
        X.append(A[i])
        continue
    elif abs(X[i-1] - B[i]) <= K and (abs(B[i] - A[i+1]) <= K or abs(B[i] - B[i+1]) <= K):
        X.append(B[i])
        continue
    else:
        break
else:
    print("Yes")
    exit()


X.clear()
X.append(B[0])
for i in range(1, N-1):
    if abs(X[i-1] - A[i]) <= K and (abs(A[i] - A[i+1]) <= K or abs(A[i] - B[i+1]) <= K):
        X.append(A[i])
        continue
    elif abs(X[i-1] - B[i]) <= K and (abs(B[i] - A[i+1]) <= K or abs(B[i] - B[i+1]) <= K):
        X.append(B[i])
        continue
    else:
        break
else:
    print("Yes")
    exit()


print("No")
