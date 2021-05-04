'''

'''
import random

def main(arr):
  temp_sum = -100
  len_arr = len(arr)
  for i in range(len_arr):
    for j in range(i+1, len_arr):
      # if temp_sum < sum(arr[i:j]):
      #   temp_sum = sum(arr[i:j])
      temp_sum = max(temp_sum, sum(arr[i:j]))
  return temp_sum

# best solution kadane's algorithm
def maximumSubarray(arr):
  globalSum = -100
  localSum = 0
  for elem in arr:
    localSum = max(elem, localSum + elem)
    globalSum = max(globalSum, localSum)
  return globalSum



#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = maximumSubarray([-3, -1, -2])
  print(s)