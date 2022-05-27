from sys import stdin


MOD = 10 ** 9 + 7


def main():
    N = int(stdin.readline())
    ans = 1
    temp_val = 1
    for _ in range(1, N+1):
        temp_val = temp_val * 4 % MOD
        ans = (ans + temp_val) % MOD

    print(ans)


if __name__ == '__main__':
    main()
