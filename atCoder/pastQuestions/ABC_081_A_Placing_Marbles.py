'''
【問題概要】

0 と 1 のみから成る 3 桁の番号 s が与えられます。1 が何個含まれるかを求めてください。

【数値例】
1)
　s = "101"
　答え: 2
'1' が 2 個含まれています。

【キーポイント】

for 文を使わない程度の全探索
string 型
'''
from typing import List

def main2021_02_02(s: int) -> int:
  counter = 0
  s = str(s)
  len_number = len(s)
  for i in range(len_number):
# int型をstring型に変えたのに、if文のときにint型を比較相手にしてしまい詰まったしまった。
    if s[i] == '1':
      counter += 1
  return counter





#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = main2021_02_02(121)
  print(s)