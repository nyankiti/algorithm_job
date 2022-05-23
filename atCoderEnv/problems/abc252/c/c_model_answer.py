from sys import stdin
"""
数字列を一つずつ探索するのではなく、先に、どの数が、どの位置にいくつ出現しているのかのカウントを取るのがポイント。
カウントが2以上であれば、2週目に突入する必要があるということ。
"""


def main():
    def check(x):
        rem = N
        for t in range(10**8):
            if count[x][t % 10] > 0:
                count[x][t % 10] -= 1
                rem -= 1
            if rem == 0:
                return t

    N = int(stdin.readline())
    slot_numbers = [input() for _ in range(N)]
    count = [[0]*10 for _ in range(10)]  # count[i][j] 数字iがj番目に出てくる回数

    for i in range(N):
        for j in range(10):
            count[int(slot_numbers[i][j])][j] += 1

    # for row in count:
    #     print(row)

    print(min(check(i) for i in range(10)))


if __name__ == '__main__':
    main()
