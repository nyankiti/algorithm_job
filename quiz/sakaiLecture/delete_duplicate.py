# input: [1,3,3,5,5,7,7,10,12,12,15] => output: [1,3,5,7,10,12,15]

from typing import List


# List内包表記による解法
l = [1, 3, 3, 5, 5, 7, 7, 10, 12, 12, 15]
[n for i, n in enumerate(l) if n not in l[:i]]


def delete_duplicate_v1(numbers: List[int]) -> None:
    temp = []
    for num in numbers:
        if num not in numbers:
            temp.append(num)

    # 数列を全て書き換える ()
    numbers[:] = temp
    # 以下のよにすると、ポインタに数列のハッシュ値?が格納されるだけで、そのポインタが参照している値は変わらない！！
    numbers = temp


if __name__ == "__main__":
    l = [1, 3, 3, 5, 5, 7, 7, 10, 12, 12, 15]
    delete_duplicate_v1(l)
    print(l)
