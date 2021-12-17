import random
# コード整理のためのtypingモジュール リストの中身のデータ型を表示して読みやすいコードが書ける
# List以外にもDict Tuple Sequenceなどがある
from typing import List


# 猿でもできるボゴソート---------------------------------------------------

# リストが並んでいるかチェック
def in_order(numbers: List[int]) -> bool:
  for i in range(len(numbers)-1):
    if numbers[i] > numbers[i+1]:
      return False
  return True
  # return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
  # 上のように書けば一行で済む


def bogo_sort(numbers: List[int]) -> List[int]:
  # リストが並ぶまでシャッフルを繰り返す
  while not in_order(numbers):
    random.shuffle(numbers)
  return numbers


# -------------------------------------------------------------------
# Bubble_sort--------------------------------------------------------
def bubble_sort_by_me(numbers: List[int]) -> List[int]:
  limit = len(numbers) - 1
  while limit > 1:
    for i in range(0, limit):
      if numbers[i] > numbers[i+1]:
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    limit = limit - 1
  return numbers

def bubble_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  for i in range(len_numbers):
      for j in range(len_numbers - 1 - i):
          if numbers[j] > numbers[j + 1]:
              numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

  return numbers

# for分が二重なのでBig_O_notationだと、O(n**2)となる


# --------------------------------------------------------------------
# Comb_sort-----------------------------------------------------------
  # combは櫛と言う意味。櫛で髪をとくようにソートするということ
  # 櫛の幅の大きさをどんどん小さくする 幅をgapという変数にいれて1.3で割りながら更新していく
def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

# どちらかの条件がTrueならループを続ける。つまり、gap=1になってもswapがある限りループが続く
    while gap != 1 or swapped:
      # gapをループごとに小さくしていく。1以下になるので１に戻す
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                swapped = True
    return numbers



# Shell_sort----------------------------------------------------------
def shell_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers // 2
    while gap > 0:
        for i in range(gap, len_numbers):
            temp = numbers[i]
            j = i
            # 一度tempにいれた値がwhile文によりgap複数回分入れ替えられうこともある
            while j >= gap and numbers[j-gap] > temp:
                numbers[j] = numbers[j-gap]
                j -= gap
            numbers[j] = temp
        gap //= 2

    return numbers






# ---------------------------------------------------------------------
# Cocktail_sort---------(別名shaker_sort)------------------------------
  # bubble_sortの改良版。swapとういうbool値が入る変数を用いて整列を判断。
  # 左右から交互に攻める

def cocktail_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  swapped = True
  # 交互に左右から整列していくのでstartとendの位置を指定しておく必要がある
  start = 0
  end = len_numbers -1
  while swapped:
    # まずはstartから整列を開始
    swapped = False
    for i in range(start,end):
      if numbers[i] > numbers[i+1]:
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        swapped = True
    # 一周、startからチェックしてswappedがFalseのままなら整列が完了しているのでwhileを抜け出す
    if not swapped:
        break
    # 逆から整列していくための処理
    swapped = False
    end = end - 1
    # ステップが-1のfor分、要素の比較を右から整列チェックする時と同じにするため、numbers[end-1]とnumbers[end]を比較
    for i in range(end - 1, start -1, -1):
        if numbers[i] > numbers[i+1]:
          numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
          swapped = True
    
    # ここでswapped=Falseのまま抜け出すと、次のwhileループに入らないので整列終了となる

    start = start + 1
  return numbers


# --------------------------------------------------------------------------------
# Gnome_sort(ノームソート)----------------------------------------------------------------------
  # Bubble_sort の改良版 一度入れ替えたら比較を一つ戻す
def gnome_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  index = 0
  while index < len_numbers:
    if index == 0:
      index += 1
    if numbers[index] >= numbers[index-1]:
      # 整列しているので順当に右にずれる
      index = index + 1
    else:
      # 整列できていないのでスイッチして、その後一つindexを戻す
      numbers[index], numbers[index-1] = numbers[index-1],numbers[index]
      index -= 1
  return numbers






#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
  nums = [random.randint(0, 1000) for _ in range(10)]
  print(bogo_sort([1,4,6,3,2]))
  print(bubble_sort([1,4,6,3,2]))
  print(cocktail_sort([1,4,6,3,2,44,24,65,7]))
  print(gnome_sort(nums))
  print(comb_sort(nums))
