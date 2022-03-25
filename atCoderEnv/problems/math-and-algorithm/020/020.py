from sys import stdin

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())

count = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            for l in range(k):
                for m in range(l):
                    if A[i] + A[j] + A[k] + A[l] + A[m] == 1000:
                        count += 1
print(count)
