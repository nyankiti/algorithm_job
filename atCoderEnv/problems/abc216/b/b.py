from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    names = {}
    for _ in range(N):
        name = input()
        if name in names:
            print("Yes")
            return
        names[name] = True

    print("No")


if __name__ == '__main__':
    main()
