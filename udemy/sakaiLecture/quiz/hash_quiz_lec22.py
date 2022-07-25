"""
1問目. Input: [11, 2, 5, 9, 10, 3], 12   => Output: (2, 10) or None
2問目. Input: [11, 2, 5, 9, 10, 3]       => Output: (11, 9) or None  ex) 11 + 9 = 2 + 5 + 10 + 3
"""

from typing import List, Tuple, Optional

def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])


# 全探索よりおしゃれな解き方
def get_pair_answer(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)




def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    # あるペアと残りの数の和が一致するということは、全体の和は2で割り切れる必要があり、2で割ったものがペアの和と一致することから解放を作る
    sum_numbers = sum(numbers)
    if sum_numbers % 2 == 1:
        return None

    half_sum = sum_numbers // 2
    
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == half_sum:
                return (numbers[i], numbers[j]) 


def get_pair_half_sum_answer(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    # sum_numbersを2で割った時の商とあまりを返す
    half_sum, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return
    
    cache = set()
    for num in numbers:
        val = half_sum - num
        if val in cache:
            return val, num
        cache.add(num)
        


if __name__ == '__main__':
    nums = [11,2,5,9,10,3]
    print(get_pair(nums, 12))

    print(get_pair_answer(nums, 12))

    print(get_pair_half_sum(nums))
    print(get_pair_half_sum_answer(nums))