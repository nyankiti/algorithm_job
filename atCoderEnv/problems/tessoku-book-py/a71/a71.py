from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    *B, = map(int, stdin.readline().split())
    A.sort()
    B.sort(reverse=True)
    ans = sum([a*b for a, b in zip(A, B)])
    print(ans)


if __name__ == '__main__':
    main()
