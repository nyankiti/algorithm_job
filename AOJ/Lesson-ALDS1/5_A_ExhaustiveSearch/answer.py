# 分割統治を法を用いたbrute forceな解法。依然として計算量は多く、TLEしてしまう実装
from sys import stdin

n = int(stdin.readline())
*table, = map(int, stdin.readline().split())
q = int(stdin.readline())
*M, = map(int, stdin.readline().split())


def recursive_search(i, sum, target):
    # 終了条件
    if sum > target:
        return False
    if i == n:
        if sum == target:
            return True
        else:
            return False

    # 選ぶ場合の分岐で組み合わせが存在した場合
    if recursive_search(i+1, sum+table[i], target):
        return True

    # 選ばない場合の分岐で組み合わせが存在した場合
    if recursive_search(i+1, sum, target):
        return True

    # # 条件を満たさなかった時(組み合わせが存在しなかった)
    return False


for m in M:
    if recursive_search(0, 0, m):
        print("yes")
    else:
        print("no")

# 20s以上かかり、LTEした。計算量はO(N^2 2^N)
