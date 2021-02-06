import random
# コード整理のためのtypingモジュール リストの中身のデータ型を表示して読みやすいコードが書ける
# List以外にもDict Tuple Sequenceなどがある
from typing import List

def insertion_sort_by_me(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  for i in range(1, len_numbers):
    temp = numbers[i]
    j = i - 1
    while j >= 0 and temp < numbers[j]:
      numbers[j + 1] = numbers[j]
      j -= 1

    # whileループの最後で j -= 1 をしているので、挿入する位置は[j+1]になるので注意
    numbers[j + 1] = temp

  return numbers



def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > temp:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = temp

    return numbers


# ---------------------------------------------------------------
# insertion_sortを利用するbucket_sort
# リストの数字を任意のバケット数を決めて分類してそれぞれをinsertion_sortで整列してからつなげる方法
# ex) バケット数を10とすると、10で割った商ごとにバケットを作る。つまり、0番台、10番台、20番台、、と分けられる

def bucket_sort(numbers: List[int]) -> List[int]:
  # バケットの数(サイズ)を決めるために最大値を取る
  max_num = max(numbers)
  len_numbers = len(numbers)
  size = max_num // len_numbers

  # バケットの数だけリストを作る
  buckets = [[] for _ in range(size)]
  # それぞれの数をバケットに振り分ける
  for num in numbers:
    # それぞれの数が入るバケットインデックスをiに格納
    i = num // size
    if i != size:
      buckets[i].append(num)
      # iとサイズが一致するｍつまりnumがサイズの基準となった最大値のときは、一番最後のバケットに追加する
    else:
      buckets[size-1].append(num)
  # バケットの中身を確認
  print(buckets)

  # バケットごとにinsrtion_sortで並び替える
  for i in range(size):
    insertion_sort(buckets[i])

  result = []
  for i in range(size):
    result += buckets[i]
  
  return result
  
# bucket_sortの計算量には O(n+k)となり、バケットをどのように分けるかによって大きく変わる
# バケットの数を整列したいListの要素の数と同じにするとO(n^2)となる
# insertion_sortの計算量がO(n^2)であるので少し計算が少なくなる

# ----------------------------------------------------------------------



if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(insertion_sort(nums))



#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  print(insertion_sort_by_me([2,33,5,67,6,4]))
  nums = [1,5,28,25,100,52,27,91,22,99]
  print(bucket_sort(nums))