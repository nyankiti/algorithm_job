from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *P, = map(int, stdin.readline().split())
    ans = [-1]*N
    for i, p in enumerate(P):
        ans[p-1] = i+1
    print(*ans)


if __name__ == '__main__':
    main()
