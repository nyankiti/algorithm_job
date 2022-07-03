from sys import stdin
import bisect


def main():
    N, K = map(int, stdin.readline().split())
    *P, = map(int, stdin.readline().split())

    li = P[:K]
    li.sort()
    print(li[-K])

    for i in range(K+1, N+1):
        bisect.insort_right(li, P[i-1])
        # print(li)
        print(li[-K])


if __name__ == '__main__':
    main()
