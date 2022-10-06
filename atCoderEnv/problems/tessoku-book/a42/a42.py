from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, stdin.readline().split())
        A.append(a)
        B.append(b)

    ans = 0
    for i in range(1, 101):
        for j in range(1, 101):
            temp = 0
            # 加減が、i, j であるとき、i+K, j+K を満たす人がサッカーに参加できる
            for k in range(N):
                if i <= A[k] and A[k] <= i + K:
                    if j <= B[k] and B[k] <= j + K:
                        temp += 1
            ans = max(ans, temp)

    print(ans)


if __name__ == '__main__':
    main()
