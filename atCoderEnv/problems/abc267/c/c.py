from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


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
    for i in range(M):
        temp_B_sum += (i+1)*A[i]
    # print(temp_B_sum)
    ans = temp_B_sum

    # 累積和を使って、ずらしながら最大のBの和を探索する
    for i in range(1, N-M+1):
        loss = (A_ruiseki[i+M-1] - A_ruiseki[i-1])
        # print("loss", str(A_ruiseki[i+M-1] -
        #       A_ruiseki[i-1]), "new", str(M*A[i+M-1]))
        temp_B_sum -= loss
        # print("after loss", str(temp_B_sum))
        temp_B_sum += (M*A[i+M-1])
        # print(temp_B_sum)

        ans = max(ans, temp_B_sum)

    print(ans)


if __name__ == '__main__':
    main()
