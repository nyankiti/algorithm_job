from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    if S[-2:] == "er":
        print("er")
    else:
        print("ist")


if __name__ == '__main__':
    main()
