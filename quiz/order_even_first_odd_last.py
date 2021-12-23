# 新しいListを生成せずに、以下のように偶数を前、奇数を後に並び替える
# input: [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8] => output: [0, 4, 2, 4, 6, 8, 1, 3, 5, 1, 9]

from typing import List


def order_even_first_odd_last(numbers: List[int]) -> None:
    # for ループ中にループしている配列自体を入れ替える操作なので、注意が必要
    # 偶数は前から、奇数は後ろからindexをつめる解法を用いる。
    even_index = 0
    odd_index = len(numbers) - 1

    while even_index < odd_index:
        if numbers[even_index] % 2 == 0:
            even_index += 1
        else:
            if numbers[odd_index] % 2 == 0:
                numbers[even_index], numbers[odd_index] = numbers[odd_index], numbers[even_index]
                odd_index -= 1
            else:
                odd_index -= 1


if __name__ == "__main__":
    l = [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8]
    order_even_first_odd_last(l)
    print(l)
