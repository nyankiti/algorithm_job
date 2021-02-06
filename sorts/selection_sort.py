def selection_sort(data):
  for i in range(0, len(data)-1):
    # とりあえずiを最小値として設定する
    min = i
    # iより小さいものをループで探しす
    for j in range(i+1, len(data)):
      if data[min] > data[j]:
        min = j
    # 見つけた最小値を未整列部の末尾と交換
    data[min], data[i] = data[i], data[min]
    

def selection_sort2(data):
  i = len(data)-1
  while i > 0:
    # とりあえずiを最大値として設定する
    max = i
    # iより小さいものをループで探す
    for j in range(0, i):
      if data[max] < data[j]:
        max = j
    # 見つけた最大値を未整列部の先端と交換
    data[max], data[i] = data[i], data[max]
    # whileのインデント処理
    i = i - 1

data = [23, 12, 55, 6, 78, 33, 4, 34, 333, 567, 2]
selection_sort2(data)
print(data)