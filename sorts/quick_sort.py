from typing import List

# 1: pivotを決める
# 2: pivotより大きい値を基準より右に置く
# 3: pivotより小さい値を基準より左に置く
# 1~3を再帰的に繰り返す

# => 基準より大きいグループと小さいグループで場合分けした時点で基準のsort後のindexが決まるのがポイント

# partitionメソッドではpivotに基づく数字の
def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[j], numbers[i] = numbers[i], numbers[j]
    # ループ後にpivotのindexがi+1と確定する
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1

# 全ての数字がpivotより小さい場合、全てのループで同じ数同士のスワップが起きる(実質スワップが起きたようには見えない)
# 全ての数字がpivotより大きい場合、ループ最中に一度もスワップが起こることなく、最後にpivotはindex=lowの位置とスワップする

def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)
            # 小さい方
            _quick_sort(numbers, low, partition_index-1)
            # 大きい方
            _quick_sort(numbers, partition_index+1, high)
    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    nums = [1,8,3,9,4,5,7]
    print(quick_sort(nums))
