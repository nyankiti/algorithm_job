import random
# コード整理のためのtypingモジュール リストの中身のデータ型を表示して読みやすいコードが書ける
# List以外にもDict Tuple Sequenceなどがある
from typing import List

def selection_sort_by_me(numbers: List[int]) -> List[int]:
  start = 0
  for j in range(len(numbers)):
    temp = start
    for i in range(start, len(numbers)):
      if numbers[temp] > numbers[i]:
        temp = i
    numbers[start], numbers[temp] = numbers[temp], numbers[start]
    start = start + 1
  return numbers

def selection_sort(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)):
      # 一時的に保存する変数名をtempではなくmin_idxとした方が意味がわかりやすい
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[min_idx] > numbers[j]:
                min_idx = j

        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
# __name__ がファイル実行時に見られる特殊変数であり
# コマンドで ファイル名.py と実行すると__name__には__main__が格納される。
# インポートでこのファイルを呼び出すと__name__にはそのファイル名が格納される
if __name__ == '__main__':
  print(selection_sort_by_me([4,5,22,3,67,1]))
  nums = [random.randint(0, 1000) for _ in range(10)]
  print(selection_sort(nums))