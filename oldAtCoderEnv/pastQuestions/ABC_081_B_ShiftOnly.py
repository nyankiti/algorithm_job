'''
【問題概要】
黒板に N 個の正の整数 A_1,…,A_N が書かれています。
すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます。

黒板に書かれている整数すべてを，2 で割ったものに置き換える。
すぬけ君は最大で何回操作を行うことができるかを求めてください。

【制約】

1≤N≤200
1≤A_i≤10^9
【数値例】
1)
　N=3
　A=(16,12,24)
　答え: 2
1 回操作を行うと (8, 6, 12) になります。2 回操作を行うと (4, 3, 6) になります。2 個目の 3 が奇数なため 3 回目の操作は行えません。

【キーポイント】

for 文を用いた全探索
シミュレーション

'''


def main2021_02_03_recursion(N, numbers):
  def _main(N, numbers):
    for i in range(N):
      if numbers[i]%2 == 1:
        return numbers
    numbers = list(map(lambda x: x//2, numbers))
    sub_result = _main(N, numbers)
    return sub_result
  result = _main(N, numbers)
  return result

def main2021_02_03(N, numbers):
  flg = True
  while (flg):
    for i in range(N):
      if numbers[i]%2 == 1:
        flg = False
        break
    if flg:
      numbers = list(map(lambda x: x//2, numbers))
  return numbers


def main(N, numbers):
  for i in range(N):
    if numbers[i]%2 == 1:
      return numbers


#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = main2021_02_02_recursion(3, [32, 64, 24])
  print(s)