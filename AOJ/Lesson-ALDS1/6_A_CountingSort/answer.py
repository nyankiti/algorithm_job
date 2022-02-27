'''
計数ソート
各要素が 0 以上 k 以下である要素数 n の数列に対して線形時間O(n+k)で動く安定なソーティングアルゴリズム。
長さがk配列を用いるため、kが大きい場合にメモリを沢山使うというデメリットがある
'''

from sys import stdin
from typing import List

n = int(stdin.readline())
*A, = map(int, stdin.readline().split())


def counting_sort(numbers: List[int]):
    max_num = max(numbers)
    counts = [0] * (max_num + 1)
    result = [0] * len(numbers)

    # countを作る
    for num in numbers:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    i = len(numbers) - 1
    while i >= 0:
        index = numbers[i]
        result[counts[index] - 1] = numbers[i]
        counts[index] -= 1
        i -= 1

    print(*result)


counting_sort(A)
