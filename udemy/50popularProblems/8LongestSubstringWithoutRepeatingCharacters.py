'''
ord() メソッドはその文字のunicodeポイントを返す
Ordinal（順序）の略で文字を渡して文字コード（コンピュータにとってのOrdinal）を求めるという意味です。
'''
from collections import defaultdict
import random


def myans(str):
    temp_sum, result = 0, 0
    visted = dict()
    for char in str:
        if visted.get(char):
            visted = dict()
            result = max(result, temp_sum)
            temp_sum = 0
        else:
            temp_sum += 1
            visted[char] = True
    return max(temp_sum, result)


'''S
longest   substring   without repeating chracters   の3つの部分に分割して考える
'''


def withoutRepeating(string):
    # アルファベットのunicodeポイントが65~122であるので
    visted = [False]*128
    for ch in string:
        if visted[ord(ch)]:
            return False
        else:
            visted[ord(ch)] = True
    return True


def LongestSubstringWithoutRepeating_(string):
    maxLength = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if withoutRepeating(substring) and len(substring) > maxLength:
                maxLength = len(substring)
    return maxLength


# best solution below
def LongestSubstringWithoutRepeating(string):
    maxLength = 0
    start = 0
    indexes = [-1]*128
    print(indexes)
    for i in range(len(string)):
        # 被りが見つかったらstart位置を変更する
        if indexes[ord(string[i])] >= start:
            start = indexes[ord(string[i])] + 1

    # 被りが見つかったときのために一度訪れた文字はその位置を記憶しておく
        indexes[ord(string[i])] = i
        maxLength = max(maxLength, i - start + 1)
    print(indexes)
    return maxLength


# best answer の改良版 default dictを用いることで、無駄に長いindexwsを使う必要を無くす
def LongestSubstringWithoutRepeating_(string):
    maxLength = 0
    start = 0
    # 以下のようにdefaultdictを定義することで、任意のkeyに対して引数のメソッドが返す値をvalueとして持つdictが生成される
    visited_indexes = defaultdict(lambda: -1)
    for i, char in enumerate(string):
        # 被りが見つかったらstart位置を変更する
        if visited_indexes[char] >= start:
            start = visited_indexes[char] + 1

    # 被りが見つかったときのために一度訪れた文字はその位置を記憶しておく
        visited_indexes[char] = i
        maxLength = max(maxLength, i - start + 1)
    return maxLength


#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
    s = LongestSubstringWithoutRepeating('abcdbeghef')
    print(s)
