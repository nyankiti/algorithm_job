'''
【問題概要】
N 個の整数 d[0],d[1],…,d[N−1] が与えられます。
この中に何種類の異なる値があるでしょうか？
(原問題文をかなり意訳していますが、題意はこういうことです)

【制約】

1≤N≤100
1≤d[i]≤100
入力値はすべて整数
【数値例】
1)
　N=4
　Q=3
　d=(8,10,8,6)
　答え: 3
6, 8, 10 の 3 種類です。


【キーポイント】

集計処理
バケット法
連想配列
'''


def main2021_02_02(a, b):



#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = main2021_02_02(3, 4)
  print(s)