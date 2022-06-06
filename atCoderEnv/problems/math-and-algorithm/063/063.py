from sys import stdin


def main():
    N = int(stdin.readline())
    print("Yes" if N % 2 == 0 else "No")


if __name__ == '__main__':
    main()
