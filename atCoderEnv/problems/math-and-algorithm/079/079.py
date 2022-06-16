from sys import stdin


def main():
    N = int(stdin.readline())
    print(N*(N-1)//2)


if __name__ == '__main__':
    main()
