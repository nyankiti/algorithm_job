from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())

    result = []

    def rec(i, li, end_num):
        if len(li) == N:
            result.append(li[:])
            return
        else:
            for j in range(end_num+1, M+1):
                li.append(j)
                rec(i+1, li, j)
                li.pop()
            return

    for i in range(1, M+1):
        rec(0, [i], i)

    for ans in result:
        print(*ans)


if __name__ == '__main__':
    main()
