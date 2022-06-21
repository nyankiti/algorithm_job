from sys import stdin


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def lmc(x, y):
    return x*y // gcd(x, y)


def main():
    A, B = map(int, stdin.readline().split())
    ans = lmc(A, B)
    if ans > 1000000000000000000:
        print("Large")
    else:
        print(ans)


if __name__ == '__main__':
    main()
