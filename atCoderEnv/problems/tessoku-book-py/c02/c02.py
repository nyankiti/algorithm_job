from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    A.sort(reverse=True)
    print(A[0]+A[1])


if __name__ == '__main__':
    main()
