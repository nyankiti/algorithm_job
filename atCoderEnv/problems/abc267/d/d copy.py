import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

# N < 2000 なので、O(N^2)まではいける


def main():
    N, M = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    # 累積和
    A_ruiseki = []
    temp_sum = 0
    for a in A:
        A_ruiseki.append(temp_sum)
        temp_sum += a

    temp_B_sum = 0
    selected = []

    for i in range(M):
        temp_B_sum += (i+1)*A[i]
        selected.append(A[i])
        # if (i+1)*A[i] < next_drop[1]:
        #     next_drop = [i, (i+1)*A[i], ]
    temp_ans = temp_B_sum

    # index, その値を省いて、indexをずらした際に生じるloss の順に記録しておく
    next_drop = [-1, math.inf]
    for i, val in enumerate(selected):
        loss = (i+1)*selected[i] + sum(selected[i+1:])
        if next_drop[1] > loss:
            next_drop = [i, loss]

    # print(next_drop)
    # print(selected)

    ans = -math.inf

    for i in range(1, N-M+1):
        if next_drop[1] + M*A[i+M-1] > 0:
            temp_ans = temp_ans - next_drop[1] + M*A[i+M-1]
            selected.pop(next_drop[0])
            selected.append(A[i+M-1])
            # 次に消去すべき値の算出
            next_drop = [-1, math.inf]
            for i, val in enumerate(selected):
                loss = (i+1)*selected[i] + sum(selected[i+1:])
                if next_drop[1] > loss:
                    next_drop = [i, loss]
            # print(i, next_drop)
            # print(selected)
        ans = max(ans, temp_ans)

        # loss = (A_ruiseki[i+M-1] - A_ruiseki[i-1])
        # temp_B_sum -= loss
        # temp_B_sum += (M*A[i+M-1])

        # temp_ans = max(temp_ans, temp_B_sum)

    print(ans)


if __name__ == '__main__':
    main()
