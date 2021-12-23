from typing import List


def get_max_sequence_sum(numbers: List[int]) -> int:
    # 結果を格納
    result_sequence = 0
    # 連続している数の合計を格納
    sum_sequence = 0

    for num in numbers:
        sum_sequence = max(num, sum_sequence + num)
        result_sequence = max(result_sequence, sum_sequence)
    return result_sequence


if __name__ == '__main__':
    print(get_max_sequence_sum([1, -2, 3, 6, -1, 2, 4, -5, 2]))
