"""
Input :["h", "y", "n", "p", "t", "o"], [3, 1, 5, 0, 2, 4]
Output: python
"""

from typing import List


# 第二引数に渡されるindexの順番で第一引数の文字を並び替える
def order_change_by_index_myans(chars: List[str], indexes: List[int]) -> str:
    dic = {index: val for index, val in zip(indexes, chars)}
    sorted_dic = sorted(dic.items(), key=lambda x: x[0])

    result = []
    for char in sorted_dic:
        result.append(char[1])
    return "".join(result)


# 先にNoneが入った配列を作って、そこに指定のindexに合わせたcharを格納する解法
def order_change_by_index_v1(chars: List[str], indexes: List[int]) -> str:
    result = [None for _ in range(len(chars))]
    # 以下のようにlist内包表記を使わなくても書ける
    # result = [None] * len(chars)

    for index, arg_index in enumerate(indexes):
        result[arg_index] = chars[index]

    return "".join(result)


# listを生成しない解法 indexesとcharsを同じタイミングで入れ替えていくのがポイント
def order_change_by_index_v2_myans(chars: List[str], indexes: List[int]) -> str:
    for i in range(len(chars)):
        if i == indexes[i]:
            continue
        else:
            alternate_index = indexes.index(i)
            indexes[i], indexes[alternate_index] = indexes[alternate_index], indexes[i]
            chars[i], chars[alternate_index] = chars[alternate_index], chars[i]
    return "".join(chars)


# listを生成しない解法 酒井さんの解法 while使う必要は特にないのでは？？
def order_change_by_index_v2(chars: List[str], indexes: List[int]) -> str:
    i, len_indexes = 0, len(indexes) - 1
    while i < len_indexes:
        if i != indexes[i]:
            alternate_index = indexes[i]
            chars[alternate_index], chars[i] = chars[i], chars[alternate_index]
            indexes[alternate_index], indexes[i] = indexes[i], indexes[alternate_index]
        i += 1
    return "".join(chars)


if __name__ == "__main__":
    print(order_change_by_index_v2(
        ["h", "y", "n", "p", "t", "o"], [3, 1, 5, 0, 2, 4]))
