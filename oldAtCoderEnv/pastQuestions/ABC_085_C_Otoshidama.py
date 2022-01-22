'''
【問題概要】
10000 円札と、5000 円札と、1000 円札が合計で N 枚あって、合計金額が Y 円であったという。このような条件を満たす各金額の札の枚数の組を 1 つ求めなさい。そのような状況が存在し得ない場合には -1 -1 -1 と出力しなさい。

【制約】

1≤N≤2000
1000≤Y≤2∗10^7
N は整数
Y は 1000 の倍数
【数値例】
1)
　N=9
　Y=45000
　答え: (4,0,5) など

10000 円札 4 枚と 1000 円札 5 枚で、合計枚数が 9 枚、合計金額が 45000 円になります。他の答えもあります。

【キーポイント】

for 文を用いた全探索
二重三重の for 文
少し工夫が必要
'''


def main2021_02_07(N, total):
  # 10000yen a枚 5000yen b枚 1000yen c枚  a+b+c = N
  a_max = total // 10000
  b_max = total // 5000
  c_max = total // 1000

  for i in range(a_max):
    sub_total = total - (i*10000)
    for j in range(b_max):
      sub_sub_total = sub_total - (j*5000)
      for k in range(c_max):
        sub_sub_sub_total = sub_sub_total - (k*1000)
        if sub_sub_sub_total == total:
          result = (i, j, k)

  print(result)
  if sum(result) != N:
    result = (-1, -1, -1)

  return result


#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = main2021_02_07(9, 45000)
  print(s)