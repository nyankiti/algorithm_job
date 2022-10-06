from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    if (N-1)*2 > K:
        print("No")
    else:
        if K % 2 == 0:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
