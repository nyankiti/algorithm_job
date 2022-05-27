from sys import stdin


def fibonacci(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for _ in range(n-1):
            a, b = b, a + b
        return b


def main():
    N = int(stdin.readline())

    print(fibonacci(N))


if __name__ == '__main__':
    main()
