from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    print(S.count("v") + S.count("w")*2)


if __name__ == '__main__':
    main()
