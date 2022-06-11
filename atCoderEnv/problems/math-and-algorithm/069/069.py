from sys import stdin


def main():
    a, b, c, d = map(int, stdin.readline().split())
    print(max(a*c, a*d, b*c, b*d))


if __name__ == '__main__':
    main()
