from typing import Counter, List
from collections import Container

def min_count_remove(x: List[int], y: List[int]) -> None:
    x_count = {}
    y_count = {}
    for v in x:
        x_count[v] = x_count.get(v, 0) + 1
    for v in y:
        y_count[v] = y_count.get(v, 0) + 1
    
    for key, value in x_count.items():
        if key in y_count:
            if value < y_count[key]:
                x.remove(key)
    
    for key, value in y_count.items():
        if key in x_count:
            if value < x_count[key]:
                y.remove(key)

    print(x)
    print(y)


def min_count_remove_answer(x: List[int], y: List[int]) -> None:
    # count_x = {}
    # count_y = {}

    # for i in x:
    #     count_x[i] = count_x.get(i, 0) + 1

    # for i in y:
    #     count_y[i] = count_y.get(i, 0) + 1
    # counterの処理は以下のようにCounter classを使うと2行で済む
    counter_x = Counter(x)
    counter_y = Counter(y)

    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x < value_y:
                # list内包表記を用いて二つ以上の数を一度に書き換える！！！！！！！
                x[:] = [i for i in x if i != key_x]
            elif value_y < value_x:
                y[:] = [i for i in y if i != key_x]


if __name__ == '__main__':
    x = [1,2,3,4,4,5,5,8,10]
    y = [4,5,5,5,6,7,8,8,10]
    print("before x: ", x)
    print("before y: ", y)

    min_count_remove_answer(x, y)
    print("after x: ",x)
    print("after y: ",y)