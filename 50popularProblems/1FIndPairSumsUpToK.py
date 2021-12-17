'''

'''
import random

# Brute force solution
def main(arr, k):
  len_arr = len(arr)
  for i in range(len_arr):
    for j in range(i+1, len_arr):
      if arr[i] + arr[j] == k:
        return True
  return False

#the answer above is not a best solution Time Conmplexity is O(n^2), Space complexisty is O(1)
# Space complexityとはアルゴリズムに使うメモリの量のこと

# second best solution
def main2(arr, k):
  arr.sort()
  left, right = 0, len(arr)-1
  while left < right:
    if arr[left] + arr[right] == k:
      return True
    elif  arr[left] + arr[right] > k:
      right -= 1
    else:
      left += 1
  return False

# k が合計より大きい時に


# best solution
# use hash table
def main3(arr, k):
  # ハッシュデーブルを宣言、ここに訪れた番号を記録しておき、kとの差がハッシュテーブルに入っていればペア成立
  visited = {}
  for element in arr:
    if visited.get(k-element):
      return True
    else:
      visited[element] = True
  return False
  # ハッシュテーブルのlook up (visited.get()の部分)の計算量はO(1)
  # ハッシュテーブルのinsertion (visited[element] = Trueの部分)の計算量もO(1)なのでこのアルゴリズムの計算量が最も小さい


  # the time complexity of this solution is O(nlogn)


#the codes in "if __name__ == '__main__': " is called when you excecute "python3 filename.py"
if __name__ == '__main__':
  s = main2([4, 5, 1, -3, 6], 11)
  print(s)
  s2 = main3([4, 5, 1, -3, 6], -2)
  print(s2)
  s3 = main3([4, 5, 1, -3, 6], 8)
  print(s3)