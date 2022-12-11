from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, T = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    A_sum = sum(A)
    T %= A_sum
    for i, a in enumerate(A):
        if T - a >= 0:
            T -= a
        else:
            print(i+1, T)
            break


if __name__ == '__main__':
    main()
