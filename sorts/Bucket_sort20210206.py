import random
'''
【問題概要】


'''


def selection_sort2021_02_06(numbers):
  len_numbers = len(numbers)
  for j in range(len_numbers):
    min_index = j
    for i in range(j+1, len_numbers):
      if numbers[min_index] > numbers[i]:
        min_index = i
    numbers[j], numbers[min_index] = numbers[min_index], numbers[j] 
  return numbers

def bucket_sort20210206(numbers):
  max_num = max(numbers)
  len_numbers = len(numbers)
  size = max_num // len_numbers
  # 引数のサイズ似合わせてバケツを作る
  buckets = [[] for _ in range(size)]
  print(buckets)
  # バケツに数字を割り当てる

  for num in numbers:
    i = num // size
  # 100が来たときは90番台と同じバケツに入るように場合分け
    if i != size:
      buckets[i].append(num) 
    else:
      buckets[size-1].append(num)
  print(buckets)
  # バケツの中をselection_sortで並び替える
  for j in range(size):
    selection_sort2021_02_06(buckets[j])
  # バケツをつなげる
  result = []
  for i in range(size):
    result += buckets[i]

  return result

#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  # s = selection_sort2021_02_06([2,45,64,4,5,78,9])
  # print(s)
  # nums = [random.randint(0,1000) for _ in range(10)]
  # a = bucket_sort20210206(nums)
  # print(a)
  for i in range(1): 
    print(i)