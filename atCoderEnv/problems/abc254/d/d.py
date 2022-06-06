from sys import stdin


def main():
    N = int(stdin.readline())
    ans = 0

    for i in range(1, N+1):
        k = i
        d = 2
        while d*d <= k:
            while k % (d * d) == 0:
                k = k // (d * d)
            d += 1

        d = 1
        while d*d*k <= N:
            ans += 1
            d += 1

    print(ans)


if __name__ == '__main__':
    main()
