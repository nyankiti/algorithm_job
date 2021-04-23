'''

'''
import random

def main(arr):
  visited = {}
  for element in arr:
    if visited.get(element):
      return element
    else:
      visited[element] = True
  return 'There was no duplicates'


#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = main([1, 4, 2, 2, 5, 2])
  print(s)