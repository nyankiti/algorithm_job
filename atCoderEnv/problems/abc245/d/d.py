from sys import stdin

N, M = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())
*C, = map(int, stdin.readline().split())

B = []
# B[0]
B.append(C[0] // A[0])

# # B[1]
# B.append((C[1] - A[1]*B[0]) // A[0])

# # B[2]
# B.append((C[2] - A[1]*B[1] - A[2]*B[0]) // A[0])

# # B[3]
# B.append((C[3] - A[1]*B[2] - A[2]*B[1] - A[3]*B[0]) // A[0])


for i in range(1, N+M):
    temp = 0
    for j in range(i):
        if i - j <= N and j < M:
            temp = temp + A[i - j] * B[j]
    # print(temp)
    b = (C[i] - temp)//A[0]
    B.append(b)

print(*B)
