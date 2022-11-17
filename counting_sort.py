from typing import List


def counting_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    # 他のソートに比べてリストを準備する数が増えるので、計算量は少ないがメモリに負担がかかる
    counts = [0] * (max_num + 1)
    result = [0] * len(numbers)

    for num in numbers:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    i = len(numbers) - 1
    while i >= 0:
        index = numbers[i]
        result[counts[index] - 1] = numbers[i]
        counts[index] -= 1
        i -= 1

    return result


# くらいに分けてcounting_sortを行うradix_sort
def radix_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    place = 1
    while max_num > place:
        numbers = counting_sort(numbers, place)
        place *= 10
    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(counting_sort(nums))