from sys import stdin, setrecursionlimit
import bisect
setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *P, = map(int, stdin.readline().split())

    j = N-2
    while P[j] < P[j+1]:
        j -= 1
    k = N-1
    while P[j] < P[k]:
        k -= 1
    P[j], P[k] = P[k], P[j]
    print(*P[:j+1], *P[:j:-1])


if __name__ == '__main__':
    main()
