from typing import List

def order_even_first_odd_last(numbers: List[int]) -> None:
  i, j = 0, len(numbers) - 1
  while i < j:
    if numbers[i] % 2 == 0:
      i += 1
    else:
      numbers[i], numbers[j] = numbers[j], numbers[i]
      j -= 1


"""
Input : ['h', 'y', 'n', 'p', 't', 'o'], [3, 1, 5, 0, 2, 4]
Output: python
"""

def order_change_by_index(chars: List[int], indexes: List[int]):
  tmp = [None] * len(chars)
  for i , index in enumerate(indexes):
    tmp[index] = chars[i]
  return ''.join(tmp)

def order_change_by_index_v2(chars: List[int], indexes[int]):
  






if __name__ == '__main__':
  l = [0,1,3,4,2,4,5,1,6,9,8]
  order_even_first_odd_last(l)
  print(l)

  a = order_change_by_index( ['h', 'y', 'n', 'p', 't', 'o'], [3, 1, 5, 0, 2, 4])
  print(a)