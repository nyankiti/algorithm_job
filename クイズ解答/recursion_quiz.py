'''
順列を表示させる関数を作る
既にpythonのライブラリにpermutationsとして用意されている permutations : 順列
from itertools import permutations
  for r in permutations([1, 2, 3]):
    print(r)
=>output
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
'''
from typing import List, Iterator

'''
recursionの考え方
  端っこから整列する 一単位の作業を徐々に全体に波及させていく時に使える
  [1,2,3,4]の順列を表示する時、まず、端の4に注目
  次に端の 3,4 に注目して、先頭である 3 を各要素の間に入れたリスト、つまり [3,4]と[4,3]を返す
  次に[2,3,4,]と[2,4,3]に注目して先頭である 2 を各要素の間に入れたリスト、つまり[2,3,4][3,2,4][3,4,2]と[2,4,3][4,2,3][4,3,2]を返す
  次に先程返された６つのリストに 1 を追加したリストを考え、先頭である 1 を各要素の間に入れたリストを返す
'''


def all_perms_v1(elements: List[int]) -> List[List[int]]:
    result = []
    if len(elements) <= 1:
        return [elements]
        # resultにappendもせず要素が一つのリストとして返す

    for perm in all_perms_v1(elements[1:]):
        for i in range(len(elements)):
                result.append(perm[:i] + elements[0:1] + perm[i:])
    return result


# def all_perms_v2(elements: List[int]) -> Iterator[List[int]]:
#     if len(elements) <= 1:
#         yield elements
#     else:
#         for perm in all_perms_v2(elements[1:]):
#             for i in range(len(elements)):
#                 yield perm[:i] + elements[0:1] + perm[i:]



# -------------------------------------------------------
# palindrome回文判定プログラム
# ------------------------------------------------------



"""
1. Check palindrome
aba => True
abc => False
racecar => True

reverseやsliceを使えば簡単にできる
s = 'test'
print(s == ''.join(reversed(s)))

print(s == s[::-1])

"""


from typing import Generator


def is_palindrome(strings: str) -> bool:
  len_strings = len(strings)
  if not len_strings:
    return False
  if len_strings == 1:
    return True
  
  start, end = 0, len_strings - 1
  while start < end:
    if strings[start] != strings[end]:
      return False
    start += 1
    end -= 1
  return True






'''

2. Find palindrome
abcracecarbda => cec, aceca, racecar

racecar
'''

def find_palindrome(strings: str, left: int, right: int) -> List:
  result = []
  while 0 <= left and right <= len(strings) - 1:
    if strings[left] != strings[right]:
      break
    result.append(strings[left: right + 1])
    left -= 1
    right += 1
  return result

def find_all_palindroem(strings: str) -> List:
  result = []
  len_strings = len(strings)
  if not len_strings:
    return result
  if len_strings == 1:
    result.append(strings)
  
  # aba
  # abba
  for i in range(1, len_strings - 1):
    for s in find_palindrome(strings, i-1, i+1):
      result.append(s)
    for s in find_palindrome(strings, i-1, i):
      result.append(s)

  return result  


  




if __name__ == '__main__':
    elements = [1, 2, 3]
    for p in all_perms_v1(elements):
        print(p)
    print('')

    print(all_perms_v1(elements))

    print(is_palindrome('raecear'))
    print(find_all_palindroem('cabac'))







