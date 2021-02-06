def insertion_sort(data):
  # インデックス０は既に整列済みと考える
    for i in range(1,len(data)):
        select = data[i]
        if data[i-1] > select:
            j = i
            data[j], data[j-1] = data[j-1], data[j]
            j -= 1
            # 整列済みのリストの中でselectより大きい
            while j > 0 and data[j-1] > select:
                data[j], data[j-1] = data[j-1], data[j]
                j -= 1
            data[j] = select

def insertion_sort1(data):
    i = len(data)-2
    while i >= 0:
        select = data[i]
        if data[i+1] < select:
            j = i
            data[j], data[j+1] = data[j+1], data[j]
            j += 1
            while j < len(data)-1 and data[j+1] < select:
                data[j], data[j+1] = data[j+1], data[j]
                j += 1
        i -= 1

data = [23, 22, 6, 78, 45, 34, 44, 69, 2, 1223]
insertion_sort1(data)
print(data)
