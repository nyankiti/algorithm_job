from sys import stdin
import collections

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())

count = 0

# 全探索ではTLEする
# for i in range(N):
#     for j in range(i):
#         if A[i] + A[j] == 500:
#             count += 1

c = collections.Counter(A)
count = c[100] * c[400] + c[200]*c[300]

print(count)
