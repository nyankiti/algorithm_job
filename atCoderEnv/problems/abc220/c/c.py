from sys import stdin


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    A_sum = sum(A)
    X = int(stdin.readline())

    ans = 0
    ans += N*(X // A_sum)

    X = X % A_sum
    for a in A:
        if X < 0:
            break
        X -= a
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
