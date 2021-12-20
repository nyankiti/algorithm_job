# 何かのコードを即興で試したい時に使うファイル
from typing import List

def list_to_int_plus_one(numbers: List[int]) -> int:
    sum_numbers = 0
    # for index, num in enumerate(numbers):
    #     sum_numbers += num * 10 ** (len(numbers) - index -1)
    for index, num in enumerate(reversed(numbers)):
        sum_numbers += num * (10 ** index)
    return sum_numbers + 1

def remove_zero(numbers: List[int]) -> None:
    if numbers and numbers[0] == 0:
        # indexが0の値を取り除く
        numbers.pop(0)
        remove_zero(numbers)


if __name__ == '__main__':
    
    print(list_to_int_plus_one([0,0,0,9,9,9,9]))

    nums = [0,1,0,0,9,9,9,9]
    remove_zero(nums)
    print(nums)


