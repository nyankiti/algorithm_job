'''
peak つまり山の天辺を求めるメソッドを考える。
'''
import random


def find_peak(arr):
    for i in range(len(err)):
        if(i == 0 or arr[i] >= arr[i+1]) and (i == len(arr)-1 or arr[i] >= arr[i+1]):
            return i+1


# binaru searchを使うと最も計算量を減らせる
def find_peak_binarysearch(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid+1]:
            left = mid+1
        else:
            right = mid
    return left


def find_peak_binarysearch(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left


#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
    s = find_peak_binarysearch([1, 999, 41, 4, 5, 8, 3, 99, 2])
    print(s)
