from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    Q = int(stdin.readline())
    for _ in range(Q):
        *query, = map(int, stdin.readline().split())
        if query[0] == 1:
            # ここの代入の計算コストを削減したい
            A = [query[1]]*N
        elif query[0] == 2:
            A[query[1]-1] += query[2]
        else:
            print(A[query[1]-1])


if __name__ == '__main__':
    main()
