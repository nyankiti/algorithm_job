'''

'''
import random

def main(arr):
  return list(set(arr))


# brute force solution
def main2(arr):
  noDuplicateArr = []
  for element in arr:
    # ここでinの探索をするのは計算量的によくない
    if element not in noDuplicateArr:
      noDuplicateArr.append(element)
  return noDuplicateArr


def main3(arr):
  if len(arr) == 0:
    return []
  arr.sort()
  # 初期値をセットしておく
  noDuplicateArr = [arr[0]]
  for i in range(1, len(arr)):
    if arr[i-1] != arr[i]:
      noDuplicateArr.append(arr[i])
  return noDuplicateArr


# 探索する時はやはりhash tableを使うのが最も効率が良い
def main4(arr):
  visited = {}
  for element in arr:
    visited[element] = True
  # dict型にkeyだけ取り出してlistにするには以下のようにする
  return list(visited.keys())



#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = main4([1,2,3,4,3,2,2,5,6,7,3,4])
  print(s)