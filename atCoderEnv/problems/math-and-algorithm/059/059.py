from sys import stdin


def main():
    N = int(stdin.readline())
    if N % 4 == 1:
        print(2)
    elif N % 4 == 2:
        print(4)
    elif N % 4 == 3:
        print(8)
    else:
        print(6)


if __name__ == '__main__':
    main()
