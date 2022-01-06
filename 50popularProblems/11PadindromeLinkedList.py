'''

'''
import random


def checkPalindrome(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[right] == arr[left]:
            left += 1
            right -= 1
        else:
            return False
    return True


#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print(checkPalindrome(arr))
