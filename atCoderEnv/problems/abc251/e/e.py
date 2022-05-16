from sys import stdin
"""
それぞれの動物について、どちらの餌をあげると安くなるかを最適化する
True => そのindex番号の餌をもらうと安い
False => 一つ前のindex番号の餌をもらうと安い
"""


def main():
    N = int(stdin.readline())

    global i
    i = 0

    def f(x):
        global i
        i += 1
        # [値段, インデックス番号] の形式で保存する
        return [int(x), i]
    *A, = map(f, stdin.readline().split())

    which_animal = []

    for i, a in enumerate(A):
        if i == N - 1:
            if a[0] <= A[0][0]:
                which_animal.append(True)
            else:
                which_animal.append(False)

        else:
            if a[0] <= A[i+1][0]:
                which_animal.append(True)
            else:
                which_animal.append(False)

    visited = {}
    cost = 0
    for i in range(1, N+1):
        visited[i] = False

    # print(which_animal)
    for i, val in enumerate(which_animal):
        if val and visited[A[i][1]+1] == False:
            visited[A[i][1]] = True
            visited[A[i][1]+1] = True
            cost += A[i][0]

    A.sort(key=lambda x: x[0])
    # print(A)
    # print(visited)
    # print(cost)

    j = 0
    while False in visited.values():
        if A[j][1] == N:
            if visited[A[j][1]] == False:
                visited[A[j][1]] = True
                visited[1] = True
                cost += A[j][0]
        else:
            if visited[A[j][1]] == False:
                visited[A[j][1]] = True
                visited[A[j][1]+1] = True
                cost += A[j][0]
        j += 1
        if j == N:
            break
    # print(visited)
    print(cost)


if __name__ == '__main__':
    main()
