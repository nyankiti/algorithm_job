from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    cylinders = [deque() for _ in range(M)]
    for i in range(M):
        k = int(stdin.readline())
        *A, = map(lambda x: int(x)-1, stdin.readline().split())
        cylinders[i].extend(A)

    # シミュレートする際に、同じ番号を取らずに得をすることはない。 => dfsなどはする必要はない
    # 各色のボールは丁度二個ずつしか存在しない。

    removable_dq = deque()
    # それぞれのシリンダーの上にきている数を管理するリスト
    top_li = [0]*N
    # 現在上に出ている値とその位置を関連付ける行列
    position_matrix = [[] for _ in range(N)]

    for i, cyl in enumerate(cylinders):
        if len(cyl) > 0:
            top_li[cyl[-1]] += 1
            position_matrix[cyl[-1]].append(i)
            if top_li[cyl[-1]] == 2:
                removable_dq.append(cyl[-1])

    # print("top li",  top_li)
    # print("removable", removable_dq)
    take_count = 0

    while removable_dq:
        take_count += 1
        target = removable_dq.pop()
        cyl_idx_1, cyl_idx_2 = position_matrix[target][0], position_matrix[target][1]
        # cylindersの値を削除
        cylinders[cyl_idx_1].pop()
        cylinders[cyl_idx_2].pop()

        # 新しく上に出てきた値の処理
        if len(cylinders[cyl_idx_1]) > 0:
            top_li[cylinders[cyl_idx_1][-1]] += 1
            position_matrix[cylinders[cyl_idx_1][-1]].append(cyl_idx_1)
            if top_li[cylinders[cyl_idx_1][-1]] == 2:
                removable_dq.append(cylinders[cyl_idx_1][-1])

        if len(cylinders[cyl_idx_2]) > 0:
            top_li[cylinders[cyl_idx_2][-1]] += 1
            position_matrix[cylinders[cyl_idx_2][-1]].append(cyl_idx_2)
            if top_li[cylinders[cyl_idx_2][-1]] == 2:
                removable_dq.append(cylinders[cyl_idx_2][-1])

        # print("top li",  top_li)
        # print("removable", removable_dq)

    print("Yes" if take_count == N else "No")


if __name__ == '__main__':
    main()
