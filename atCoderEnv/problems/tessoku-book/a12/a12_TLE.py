from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    # シュミレート
    count = 0
    time = 1
    while count < K:
        for a in A:
            if time % a == 0:
                count += 1
        if count < K:
            time += 1
    print(time)


if __name__ == '__main__':
    main()
