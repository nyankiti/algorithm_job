'''

'''
import random


def gesSubStringIndex(str1, str2):
    len_str2 = len(str2)
    for i in range(0, len(str1)-len_str2+1):
        if str1[i: i + len_str2] == str2:
            return i
    return -i


# スライスを使わない解法(二重に探索する)
def getSubStringIndex_v2(str1, str2):
    n = len(str1)
    m = len(str2)
    for i in range(n-m + 1):
        found = True
        for j in range(m):
            if str1[i+j] != str2[j]:
                found = False
                break
        if found:
            return i
    return -1


#  if __name__ == '__main__': の分の中の処理は python3 sorts.py とコマンドで呼び出した時に自動的に呼ばれる
if __name__ == '__main__':
    s = gesSubStringIndex("insidijihside", "side")
    print(s)
