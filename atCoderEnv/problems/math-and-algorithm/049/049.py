from sys import stdin

MOD = 1000000007


def main():
    N = int(stdin.readline())

    def fibonacci(n):
        fk, fk_1 = 1, 1
        for _ in range(n):
            fk, fk_1 = fk_1 % MOD, (fk + fk_1) % MOD

        return fk
    print(fibonacci(N-1))


if __name__ == '__main__':
    main()
