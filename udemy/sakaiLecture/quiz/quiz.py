from typing import Tuple
import operator
from collections import Counter

# タプル文字と数字で返すときはoeprator の itemgetter を使いこなすのがポイント
# タプルの内、数字の要素だけを見て、sum.countなどのメソッドを使いたい時に、タプルのインデックス番号
# をitemgetter の引数に渡せば使えるようになる

def count_chars_v1(strings: str) -> Tuple[str, int]:
  strings = strings.lower()
  l = []
  for char in strings:
    if not char.isspace():
      l.append((char, strings.count(char)))

  return max(l, key=operator.itemgetter(1))


# dict型を使った方法
def count_chars_v2(strings: str) -> Tuple[str, int]:
  strings = strings.lower()
  d = dict()
  for char in strings:
    if not char.isspace():
      # dict型のgetメソッドではその値が取れる。値がまだ入っていない時のデフォルト値を第二引数に渡せる
      d[char] = d.get(char, 0) + 1
    max_key = max(d, key=d.get)
    # 定義内ではdict型を使ったが、返り値はtupleとして返す
    return max_key, d[max_key]



# ----------------------------------------------------------
# ２つのリストに出現する数が少ない値をリストから消去する問題
# Input  X: [1, 2, 3, 4, 4, 5, 5, 8, 10] Y: [4, 5, 5, 5, 6, 7, 8, 8, 10]
# =>   X: [1, 2, 3, 4, 4, 10]          Y: [5, 5, 5, 6, 7, 8, 8, 10]
# ----------------------------------------------------------

def min_count_remove_by_me(x :List[int], y: List[int]) -> None:
  # dict型でそれぞれの値をカウントしていくのがポイント
  count_x = {}
  count_y = {}
  # まずそれぞれのカウントを作るためのループ
  for i in range(len(x)):
    if not count_x[x[i]]:
      count_x[x[i]] = 0
    count_x[i] +=1
  for i in range(len(y)):
    if not count_y[y[i]]:
      count_y[y[i]] = 0
    count_y[y[i]] +=1

  # カウントを比べて消去する
  for i in range(len(count_x)):
    for j in range(len(count_y)):
      if count_x[i] == count_y[j]:
        if count_x


def min_count_remove(x: List[int], y: List[int]) -> None:
    # counter_x = {}
    # counter_y = {}
    # for i in x:
    #     counter_x[i] = counter_x.get(i, 0) + 1
    # for i in y:
    #     counter_y[i] = counter_y.get(i, 0) + 1

    # Counter を使えばリストの同じ値を勝手に辞書型にしてカウントしてくれる
    counter_x = Counter(x)
    counter_y = Counter(y)

# 辞書型はkeyとvalueを下記のうように一緒にループできる
    for key_x, value_x in counter_x.items():
      # xだけをループしてyはループ中の値を使って呼び出しながら比べるのがポイント
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x < value_y:
              # リストの書き換え
              # x.remove()関数では重複した値を消すことは出来ない
                x[:] = [i for i in x if i != key_x]
            elif value_x > value_y:
              # リストの書き換え
                y[:] = [i for i in y if i != key_x]






if __name__ == '__main__':
  s = "This is a pen. This is an apple. applepen"
  print(count_chars_v1(s))