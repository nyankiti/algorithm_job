'''
全探索するなら、2^len(arr)通りという莫大な探索が必要
kadaneのアルゴリズムが良い
'''
import random

# kadane's algorithm


def maximumSubarray(arr):
    result, tempSum = 0, 0
    for num in arr:
        tempSum += num
        tempSum = max(tempSum, num)
        result = max(result, tempSum)
    return result


# brute force
def bruteForce(arr):
    result = 0
    len_arr = len(arr)
    for i in range(len_arr):
        temp_sum = 0
        for j in range(i, len_arr):
            temp_sum += arr[j]
            result = max(result, temp_sum)
    return result


    #  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
    s = maximumSubarray([2, 3, -6, 4, 2, -8, 3])
    print(s)
    s = bruteForce([2, 3, -6, 4, 2, -8, 3])
    print(s)
