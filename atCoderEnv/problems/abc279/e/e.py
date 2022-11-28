from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    # 0 の一だけを追いかけておけば良い。
    zero_pos = 0
    for i in range(M):
        pass


if __name__ == '__main__':
    main()
