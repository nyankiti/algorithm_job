'''

'''
import random


def main(string):
    ls = []
    for i in range(len(string)):
        if string[i] in ls:
            return string[i]
        ls.append(string[i])
        # pythonで \0 は null を意味する
    return '\0'


#  best solution which explained in udemy course
#  use hash tabel
#  inを用いたlistの探索は計算量がO(n)になるのに対し、hashtableの探索は計算量がO(1)なので早くなる
def main2(string):
    visited = {}
    for ch in string:
        if visited.get(ch):
            return ch
        else:
            visited[ch] = True
    return '\0'


#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
    s = main('inside code')
    print(s)
    s1 = main('programming')
    print(s1)
    s2 = main('abcd')
    print(s2)
