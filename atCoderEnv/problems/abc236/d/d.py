from itertools import combinations, permutations
from sys import stdin, setrecursionlimit
from typing import List

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    # 相性を格納しておく行列(iとjの相性と、jとiの相性は同じなので、対称行列)
    compatibilities = [[-1]*(2*N) for _ in range(2*N)]

    for i in range(2*N):
        *A, = map(int, stdin.readline().split())
        for j in range(len(A)):
            compatibilities[i][i+j+1] = A[j]
            compatibilities[j+i+1][i] = A[j]
    # for row in compatibilities:
    #     print(row)
    global ans
    ans = 0

    # dfsで二人組を作っていく。未分類の人の配列を持つ必要がある
    def dfs(is_selected: List[bool], x):
        global ans

        start_index = -1
        # 残っている人の中で、最も早い人
        for i in range(2*N-1):
            if is_selected[i] == False:
                start_index = i
                break

        # 全ての人が選択されている場合がbase case
        if start_index == -1:
            ans = max(ans, x)
            return

        is_selected[start_index] = True
        for i in range(2*N):
            if is_selected[i] == False and start_index != i:
                is_selected[i] = True
                dfs(is_selected, x ^ compatibilities[start_index][i])
                is_selected[i] = False
        is_selected[start_index] = False

    is_selected = [False]*(2*N)
    dfs(is_selected, 0)

    print(ans)


if __name__ == '__main__':
    main()
