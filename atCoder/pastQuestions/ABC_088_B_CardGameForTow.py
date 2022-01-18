'''
【問題概要】
N 枚のカードがあり、i 枚目のカードには ai という数が書かれています。
Alice と Bob はこれらのカードを使ってゲームを行います。ゲームでは 2 人が交互に 1 枚ずつカードを取っていきます。Alice が先にカードを取ります。
2 人がすべてのカードを取ったときゲームは終了し、取ったカードの数の合計がその人の得点になります。2 人とも自分の得点を最大化するように最適戦略をとったとき、Alice は Bob より何点多くの得点を獲得できるかを求めてください。

【制約】

N は 1 以上 100 以下の整数
ai は 1 以上 100 以下の整数
【数値例】
1)
　N=3
　a=(2,7,4)
　答え: 5
以下が最適です:

1 ターン目: Alice が 7 を取る
2 ターン目: Bob が 4 を取る
3 ターン目: Alice が 2 を取る
Alice は 7 + 2 = 9 点、Bob は 4 点を獲得するので、その差は 9 - 4 = 5 点です。

【キーポイント】

ソート
Greedy
'''


def main2021_02_07(N, numbers):
  numbers = sorted(numbers)
  print(numbers)
  a_score = 0
  b_score = 0
  for i in range(N):
    if i%2 == 0:
      a_score += numbers[i]
    else:
      b_score += numbers[i]
  result = a_score - b_score
  print(a_score)
  print(b_score)
  return result

'''
sorted(numbers)   並び替えられた結果を返す。
numbers.sort()   配列自体を並び替えてしまう。

'''

#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = main2021_02_07(3, (2,7,4))
  print(s)