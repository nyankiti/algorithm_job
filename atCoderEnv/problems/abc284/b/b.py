from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    T = int(stdin.readline())
    for _ in range(T):
        N = int(stdin.readline())
        *A, = map(int, stdin.readline().split())
        ans = 0
        for a in A:
            if a % 2 == 1:
                ans += 1
        print(ans)


if __name__ == '__main__':
    main()
