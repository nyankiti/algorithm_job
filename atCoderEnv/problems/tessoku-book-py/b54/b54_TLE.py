from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    A = [int(stdin.readline()) for _ in range(N)]
    A.sort()
    ans = 0
    for i, a in enumerate(A):
        j = i+1
        while j < N and A[j] == a:
            ans += 1
            j += 1
    print(ans)


if __name__ == '__main__':
    main()
