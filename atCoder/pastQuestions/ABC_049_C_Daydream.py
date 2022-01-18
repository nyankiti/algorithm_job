'''
【問題概要】
英小文字からなる文字列 S が与えられます。
T が空文字列である状態から始めて、以下の操作を好きな回数繰り返すことで S=T とすることができるか判定してください。

T の末尾に "dream", "dreamer", "erase", "eraser" のいずれかを追加する。
【制約】

1≤|S|≤10^5
S は英小文字からなる
【数値例】
1)
　S = "dreameraser"
　答え: "YES"

"dream", "eraser" の順で T の末尾に追加することで S=T とすることができます。

【キーポイント】

Greedy アルゴリズム
端から決まって行く Greedy アルゴリズム
後ろから解く
'''
import random

def main2021_02_08(S):
  T = ''
  lists = ["dream", "dreamer", "erase", "eraser"]
  while len(S) > len(T):
    num = random.randint(0, 3)
    T = T + lists[num]
    if S == T:
      return 'YES'
  return 'NO'

def main2021_02_09(S):
  T = ''
  lists = ["dream", "dreamer", "erase", "eraser"]
  candidate = []

  for i in range(4):
    T = T + lists[i]
    candidate.append(T)
    for j in range(4):
      candidate.append(T + lists[j])
      print(candidate)
    T = ''
  if S in candidate:
    return 'YES'
  print("dream" in candidate)
  return 'NO'


def main2021_02_14(query):
  while 1:
    for flag in ["dream", "dreamer", "erase", "eraser"]:
      if query.endswith(flag):
        # スライスを用いて後ろから削っていくことがポイント
        query = query[:-len(flag)]
        break
      else:
        print("NO")
        break
      
      if not query:
        print('YES')
        break




def main2021_02_10(S):
  T = ''
  lists = ["dream", "dreamer", "erase", "eraser"]
  candidate = []

#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = main2021_02_09("dreameraser")
  print(s)