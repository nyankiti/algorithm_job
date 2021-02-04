'''
【問題概要】
1以上 N 以下の整数のうち、10 進法で各桁の和が A 以上 B 以下であるものについて、総和を求めてください。

【制約】

1≤N≤10^4
1≤A≤B≤36
入力はすべて整数
【数値例】
1)
　N=20
　A=2
　B=5
　答え: 84
20 以下の整数のうち、各桁の和が 2 以上 5 以下なのは、2, 3, 4, 5, 11, 12, 13, 14, 20 です。これらの合計である 84 を出力します。



'''

# int型の桁をstr型に変換することでスライスを用いて分ける方法
def main2021_02_04(N, A, B):
  result = []
  # ①リスト内包表記でそれぞれのstr型の数字のリストにする
  # ②map関数でリストのそれぞれの要素をint型に戻す
  # ③int型に戻した配列の和を取る
  for i in range(N + 1):
    M = str(i)
    each_disital_sum = sum(map(lambda x: int(x) , [M[j] for j in range(len(M))]))
    if each_disital_sum >= A and each_disital_sum <= B:
      result.append(int(M))

  print(result)
  result = sum(result)

  return result

'''
10進数の特徴を活かした解放

例えば 834 の各桁の和は 8 + 3 + 4 = 15 ですが、このような処理をプログラムする方法を考えなければなりません。これには以下のような定石があります:

834 を 10 で割った余りは 4 -> 答えに加算
834 を 10 で割って 83
83 を 10 で割った余りは 3 -> 答えに加算
83 を 10 で割って 8
8 を 10 で割った余りは 8 -> 答えに加算
8 を 10 で割って 0
0 なので break

下記で書いたfindSumOfDigits関数をよく使うので覚えておいても良い
'''
def findSumOfDigits(n):
  sumOfDigits = 0
  while(n > 0):
    sumOfDigits += n % 10;
    n = n // 10
  return sumOfDigits

def main(N, A, B):
  result = []
  for i in range(N + 1):
    sumOfDigits = findSumOfDigits(i)
    if sumOfDigits >= A and sumOfDigits <= B:
      result.append(int(i))

  return sum(result)


#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  s = main(45, 2, 6)
  print(s)

  a = main2021_02_04(45, 2, 6)
  print(a)