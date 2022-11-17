# 後ろから整列済みになるアルゴリズム
def bubble_sort(data):
    for i in range(0, len(data) - 1):
        for j in range(1, len(data) - i):
            if data[j - 1] > data[j]:
                data[j], data[j - 1] = data[j -
                                            1], data[j]  #インデックスj-1とjを入れ替える処理


def bubble_sort2(data):
    for i in range(0, len(data) - 1):
        j = len(data) - 1
        while j >= i + 1:
            if data[j - 1] > data[j]:
                data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1


data = [21, 10, 80, 2, 43, 55, 77, 3, 4]
bubble_sort2(data)
print(data)