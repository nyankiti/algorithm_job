from typing import List


def snake_string_myans_v1(chars: str) -> List[List[str]]:
    result = [[], [], []]
    for index, char in enumerate(chars):
        if index % 4 == 0:
            result[1].append(char)
            result[0].append(" ")
            result[2].append(" ")
        elif index % 4 == 1:
            result[0].append(char)
            result[1].append(" ")
            result[2].append(" ")
        elif index % 4 == 2:
            result[1].append(char)
            result[0].append(" ")
            result[2].append(" ")
        elif index % 4 == 3:
            result[2].append(char)
            result[0].append(" ")
            result[1].append(" ")

    print("".join(result[0]))
    print("".join(result[1]))
    print("".join(result[2]))


def snake_string_v1(chars: str) -> List[List[str]]:
    result = [[], [], []]
    # indexをsetに入れて管理する
    result_index = {0, 1, 2}
    insert_index = 1

    for index, char in enumerate(chars):
        if index % 4 == 1:
            insert_index = 0
        elif index % 2 == 0:
            insert_index = 1
        elif index % 4 == 3:
            insert_index = 2
        result[insert_index].append(char)

        rest_indexes = result_index - {insert_index}
        for rest_index in rest_indexes:
            result[rest_index].append(" ")

    return result


def snake_string_v2(chars: str, depth: int) -> List[List[int]]:
    result = [[] for i in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth // 2)

    def positive(i): return i + 1

    def negative(i): return i - 1

    operator = negative

    for char in chars:
        result[insert_index].append(char)
        rest_indexes = result_indexes - {insert_index}
        for rest_index in rest_indexes:
            result[rest_index].append(" ")
        if insert_index <= 0:
            operator = positive
        if insert_index >= depth - 1:
            operator = negative
        insert_index = operator(insert_index)

    return result


if __name__ == '__main__':
    # ネストしたList内包表記
    numbers = [str(i) for j in range(5) for i in range(10)]
    strings = "".join(numbers)

    for line in snake_string_v1(strings):
        print("".join(line))

    alphabet = [s for _ in range(2) for s in "abcdefghijklmnopqrstuvwxys"]
    strings = "".join(alphabet)

    for line in snake_string_v2(strings, 5):
        print("".join(line))
