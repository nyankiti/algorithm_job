from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    # 答えで二分探索
    def check(x):
        print_count = 0
        for a in A:
            print_count += x//a

        if print_count >= K:
            return True
        else:
            return False

    min_time = 1
    max_time = 10**9
    while min_time < max_time:
        middle_time = (min_time + max_time)//2
        res = check(middle_time)
        if res:
            max_time = middle_time
        else:
            min_time = middle_time+1

    print(max_time)


if __name__ == '__main__':
    main()
