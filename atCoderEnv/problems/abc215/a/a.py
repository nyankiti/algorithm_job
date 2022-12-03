from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    print("AC" if S == "Hello,World!" else "WA")


if __name__ == '__main__':
    main()
