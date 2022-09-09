from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    A, B, C = map(int, stdin.readline().split())

    for i in range(1, 1000):
        if A <= C*i and C*i <= B:
            print(C*i)
            return
    print(-1)


if __name__ == '__main__':
    main()
