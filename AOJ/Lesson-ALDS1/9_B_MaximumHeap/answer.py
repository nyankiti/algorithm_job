from sys import stdin, maxsize

H = int(stdin.readline())
# heapの最初に番兵を入れる必要があるので注意！！
# (index = 0 は left child nodeのindexが0となることから分かるように、バグるので最初に大きな値を入れて対応する)
*A, = maxsize, *map(int, stdin.readline().split())


def maxHeapify(A, index):
    left_child_index = 2*index
    right_child_index = 2*index+1

    if left_child_index <= H and A[left_child_index] > A[index]:
        largest = left_child_index
    else:
        largest = index
    if right_child_index <= H and A[right_child_index] > A[largest]:
        largest = right_child_index

    # 子の方が値が小さい場合、swapする
    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        # 再帰的に呼び出す(子nodeのindexがHより小さくなって終了する)
        maxHeapify(A, largest)


def buildMaxHeap(A):
    for i in range(H//2, 0, -1):
        maxHeapify(A, i)


buildMaxHeap(A)

print("", *A[1:])


'''
00.80 s
60328 KB
3388902 B
3388896 B
6.in
'''
