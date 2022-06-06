from sys import stdin


def main():
    N = int(stdin.readline())
    if N % 4 == 0:
        print("Second")
    else:
        print("First")


if __name__ == '__main__':
    main()
