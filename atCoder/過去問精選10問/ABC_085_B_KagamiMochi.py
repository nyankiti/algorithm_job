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

# setを使えば楽勝の問題
def main2021_02_04_by_using_set(N, d):
  set1 = set(d)
  result = len(set1)
  return result


'''
バケット法
予め順番通りに並べて準備されたバケツにデータをほりこむことでソートする（別名バケツ法）
データが存在する範囲が有限個に制限されてると有用  ※データが無限にあるとバケツの用意するためにメモリに負担をかけてしまう

これらのカードを、数字が小さい順に並べ替えるのに、バケットソートでは、1～100までの数字が横に書かれている100個のバケツを準備します。
そして、カードを適当に取り出して、その番号と一致するバケツに放り込みます。また、別なカードを取り出しては、対応するバケツに放り込みます。

'''
def main2021_02_04(N, d):
  countedList = []
  for i in range(N):
    for j in range(len(countedList)):
      if d[i] == countedList[j]:
        break
    
    countedList.append(d[i])



#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = main2021_02_02(4, (8,10,8,6,10,3,4,10))
  l = [i for i in range(4)]
  print(s)