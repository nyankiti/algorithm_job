'''
1~nの数がn+1の長さの配列に格納された入力を受け取る。ただし、重複する数は一つとする
pigeonhole principleより、必ず一つの数は重複していることがわかる。
Floyd's cycle detection algorithmを用いることができる重要な問題
'''
import random


def main(arr):
    visited = {}
    for element in arr:
        if visited.get(element):
            return element
        else:
            visited[element] = True
    return 'There was no duplicates'


def findDuplicateTortoiseHare(arr):
    tortoise = arr[0]
    hare = arr[arr[0]]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
    tortoise = 0
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]
    return tortoise


#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
    s = main([1, 4, 2, 2, 5, 2])
    print(s)
    ss = findDuplicateTortoiseHare([1, 4, 2, 2, 5, 2])
    print(ss)
