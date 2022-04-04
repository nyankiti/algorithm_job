from sys import stdin
from typing import List

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())


def merge_sort(A):
    if len(A) <= 1:
        return A

    middle = len(A) // 2
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])

    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


res = merge_sort(A)
print(*res)


# 以下のように、新しい配列を生成するのではなく、swapしながらソートする方法だと、メモリ量が少なくて済む
def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    left_index = right_index = result_index = 0

    while left_index < len(left) and right_index < len(right):
        if (left[left_index] <= right[right_index]):
            numbers[result_index] = left[left_index]
            left_index += 1
        else:
            numbers[result_index] = right[right_index]
            right_index += 1
        result_index += 1

    while left_index < len(left):
        numbers[result_index] = left[left_index]
        left_index += 1
        result_index += 1

    while right_index < len(right):
        numbers[result_index] = right[right_index]
        right_index += 1
        result_index += 1

    return numbers
