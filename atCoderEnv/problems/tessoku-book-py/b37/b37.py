from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    N_digit = len(str(N))

    ans = 0
    for digit in range(16):
        for num in range(1, 10):
            count_full = N // (10 ** (digit + 1)) * 10**digit
            count_half = min(max(0, N % (10 ** (digit + 1)) -
                             (num * 10**digit - 1)), 10**digit)
            ans += num * (count_full + count_half)
    print(ans)


if __name__ == '__main__':
    main()
