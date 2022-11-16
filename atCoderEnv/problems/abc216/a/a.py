from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    X, Y = input().split(".")
    Y = int(Y)
    if 0 <= Y and Y <= 2:
        print(X+"-")
    elif 3 <= Y and Y <= 6:
        print(X)
    else:
        print(X+"+")


if __name__ == '__main__':
    main()
