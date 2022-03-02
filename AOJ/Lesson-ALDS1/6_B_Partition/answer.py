from sys import stdin

n = int(stdin.readline())
*A, = map(int, stdin.readline().split())

def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


partition_index = partition(A, 0, len(A)-1)
print(*A[:partition_index], "", end="")
print("[%d]"%(A[partition_index]), "", end="")
print(*A[partition_index+1:])