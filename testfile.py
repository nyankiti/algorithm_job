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

    money = 300
    item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300),
            ("さくらんぼ", 150), ("バナナ", 170), ("りんご", 120))
    len_item = len(item)
    for i in range(2 ** len_item):
        bag = []
        print("pattern {}: ".format(i), end="")
        for j in range(len_item):
            if ((i >> j) & 1):
                bag.append(item[j][0])
        print(bag)
