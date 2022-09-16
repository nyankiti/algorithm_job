from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *P, = map(int, stdin.readline().split())

    # 与えられた配置で喜ぶ人の人数を算出するメソッド
    def check(li):
        res = 0
        right_weight = 0
        left_weight = 0
        for i, p in enumerate(li):
            if i == p:
                res += 1
            elif i == li[(i-1) % N]:
                res += 1
                left_weight += 1
            elif i == li[(i+1) % N]:
                res += 1
                right_weight += 1
        next_direction = right_weight < left_weight
        return res, next_direction

    # 二分探索で調べられる?
    ans = 0
    left_index = 0
    right_index = N
    while left_index <= right_index:
        middle_index = (left_index+right_index)//2
        middle_value, next_direction = check(P[middle_index:]+P[:middle_index])

        ans = max(ans, middle_value)

        if next_direction:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1

    print(ans)


if __name__ == '__main__':
    main()
