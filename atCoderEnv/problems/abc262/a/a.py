from sys import stdin


def main():
    Y = int(stdin.readline())

    while Y % 4 != 2:
        Y += 1
    print(Y)


if __name__ == '__main__':
    main()
