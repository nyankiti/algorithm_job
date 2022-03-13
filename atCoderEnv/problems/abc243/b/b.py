from sys import stdin

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())
*B, = map(int, stdin.readline().split())

count_1 = 0
count_2 = 0

for index, value in enumerate(A):
    if value == B[index]:
        count_1 += 1
    elif value in B:
        count_2 += 1

print(count_1)
print(count_2)
