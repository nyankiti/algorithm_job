from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    takahashi_A, aoki_B = map(int, stdin.readline().split())
    problems = {
        1: False,
        2: False,
        4: False
    }

    def check(point):
        if point == 1:
            problems[1] = True
        elif point == 2:
            problems[2] = True
        elif point == 3:
            problems[1] = True
            problems[2] = True
        elif point == 4:
            problems[4] = True
        elif point == 5:
            problems[1] = True
            problems[4] = True
        elif point == 6:
            problems[2] = True
            problems[4] = True
        elif point == 7:
            problems[1] = True
            problems[2] = True
            problems[4] = True
    check(takahashi_A)
    check(aoki_B)
    ans = 0
    for key in problems.keys():
        if problems[key]:
            ans += key
    print(ans)


if __name__ == '__main__':
    main()
