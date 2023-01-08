from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    # 答えで二分探索
    min_time, max_time = 1, 10**9
    while min_time < max_time:
        middle_time = (min_time + max_time)//2

        print_count = 0
        for a in A:
            print_count += middle_time//a

        if print_count < K:
            min_time = middle_time + 1
        else:
            max_time = middle_time

    print(max_time)


if __name__ == '__main__':
    main()
