'''

'''
import random
from collections import defaultdict


# 自分の最初の回答。bool値のvisitedを使うと可読性がゴミすぎる
def longestPossiblePalindromeMyans(string: str):
    count, result = 0, 0
    visited = defaultdict(lambda: False)
    for char in string:
        if visited.get(char):
            count += 1
            visited[char] = False
        else:
            visited[char] = True

    if True in visited.values():
        result = count * 2 + 1
    else:
        result = count * 2

    return result


# counterを使うとわかりやすい。奇数個しかカウントされない文字があるかどうかは、resultとlen(string)の比較によって判断する
def longestPossiblePalindrome(string: str):
    result = 0
    counter = defaultdict(int)
    for char in string:
        counter[char] += 1
    for occu in counter.values():
        if occu % 2 == 0:
            result += occu
        else:
            result = result + occu - 1
    # 中心に文字を置ける場合は１をインクリメントしておく
    if result < len(string):
        result += 1

    return result


    #  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
    s = longestPossiblePalindrome("abdcRr")
    print(s)
