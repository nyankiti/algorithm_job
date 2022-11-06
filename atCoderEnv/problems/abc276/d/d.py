from sys import stdin, setrecursionlimit
import math

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    def divide(x):
        two_count, three_count = 0, 0
        while x % 2 == 0:
            two_count += 1
            x //= 2
        while x % 3 == 0:
            three_count += 1
            x //= 3
        return {2: two_count, 3: three_count, "rest": x}

    # {2: count, 3: count, rest: number}
    two_three_factor = [divide(a) for a in A]
    # print(two_three_factor)
    rest_val = two_three_factor[0]["rest"]
    min_two_count = math.inf
    min_three_count = math.inf
    ans = 0
    for val in two_three_factor:
        min_two_count = min(min_two_count, val[2])
        min_three_count = min(min_three_count, val[3])
        ans += (val[2]+val[3])
        if rest_val != val["rest"]:
            print(-1)
            return

    ans -= min_two_count*N
    ans -= min_three_count*N
    # print(min_two_count, min_three_count)
    print(ans)


if __name__ == '__main__':
    main()
