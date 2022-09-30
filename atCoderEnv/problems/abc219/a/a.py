from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    X = int(stdin.readline())
    if 0 <= X and X < 40:
        print(40-X)
    elif 40 <= X and X < 70:
        print(70-X)
    elif 70 <= X and X < 90:
        print(90-X)
    else:
        print("expert")


if __name__ == '__main__':
    main()
