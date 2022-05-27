from sys import stdin


def main():
    N, X, Y = map(int, stdin.readline().split())

    if N < abs(X)+abs(Y):
        print("No")
    else:
        if N % 2 == (X+Y) % 2:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
