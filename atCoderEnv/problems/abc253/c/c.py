from sys import stdin
import bisect
# 配列を二分探索によってsortされた状態を維持しながら作る。
# counterを別で用意する


def main():
    Q = int(stdin.readline())
    counter = {}
    numbers = []
    flg = True

    for _ in range(Q):
        *query, = map(int, stdin.readline().split())
        if query[0] == 1:
            x = query[1]
            counter[x] = counter.get(x, 0) + 1
            bisect.insort(numbers, x)

        elif query[0] == 2:
            x = query[1]
            rm_count = min(query[2], counter.get(x, 0))
            for _ in range(rm_count):
                rm_index = bisect.bisect_left(numbers, x)
                numbers.pop(rm_index)

        elif query[0] == 3:
            flg = False
            print(numbers[-1] - numbers[0])
    if flg:
        print()


if __name__ == '__main__':
    main()
