'''

'''
import random

def main(numbers):
  for i in range(0, len(numbers)-1):
    if numbers[i] <= numbers[i+1]:
      if i+2 == len(numbers):
        return i+1
      elif numbers[i+1] >= numbers[i+2]:
        return i+1

def find_peak(arr):
  for i in range(len(err)):
    if(i == 0 or arr[i] >= arr[i+1]) and (i == len(arr)-1 or arr[i] >= arr[i+1]):
      return i+1

# binaru searchを使うと最も計算量を減らせる
def find_peak_binarysearch(arr):
  left = 0
  right = len(arr)-1
  while left < right:
    mid = (left + right) // 2
    if arr[mid] < arr[mid+1]:
      left = mid+1
    else:
      right = mid
  return left



#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = find_peak_binarysearch([4,5,8,3])
  print(s)