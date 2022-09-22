from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] + A[j] + A[k] == 1000:
                    print("Yes")
                    return
    print("No")


if __name__ == '__main__':
    main()
