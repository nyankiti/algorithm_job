from sys import stdin, maxsize
from typing import List

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())
# 番兵の追加
A = [maxsize] + A


def max_heapify(A, index, heap_size):
    left_child_index = 2*index
    right_child_index = 2*index+1

    if left_child_index <= heap_size and A[left_child_index] > A[index]:
        largest = left_child_index
    else:
        largest = index
    if right_child_index <= heap_size and A[right_child_index] > A[largest]:
        largest = right_child_index

    # 子の方が値が小さい場合、swapする
    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        # 再帰的に呼び出す(子nodeのindexがHより小さくなって終了する)
        max_heapify(A, largest, heap_size)


def heap_sort(A: List[int], N: int):
    heap_size = N

    # heapの構築
    for i in range(N//2, 0, -1):
        max_heapify(A, i, N)

    # sort
    while heap_size >= 2:
        # 1番目に格納されている最も大きい値を最後尾へ格納することを繰り返す
        A[1], A[heap_size] = A[heap_size], A[1]
        heap_size -= 1
        max_heapify(A, 1, heap_size)


heap_sort(A, N)


for i in range(2, N):
    print(A)
    A[1], A[i] = A[i], A[1]
    # while文を用いて最も小さい値をrootまで戻す
    while i != 1:
        A[i], A[i//2] = A[i//2], A[i]
        i //= 2
A[1], A[N] = A[N], A[1]

print(*A[1:])
