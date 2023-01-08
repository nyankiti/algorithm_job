from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, Q = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    temp_sum = 0
    ruiseki = [temp_sum]

    for a in A:
        temp_sum += a
        ruiseki.append(temp_sum)

    for _ in range(Q):
        L, R = map(int, stdin.readline().split())
        print(ruiseki[R] - ruiseki[L-1])


if __name__ == '__main__':
    main()
