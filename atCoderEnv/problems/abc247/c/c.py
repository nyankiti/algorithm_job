from sys import stdin


def main():
    N = int(stdin.readline())

    def f(n, s):
        if n == 1:
            return "1"
        return f(n-1, s) + " " + str(n) + " " + f(n-1, s)

    print(f(N, ""))


if __name__ == '__main__':
    main()
