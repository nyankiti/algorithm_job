from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    schedule = [list(map(int, stdin.readline().split())) for _ in range(N)]
    schedule.sort(key=lambda x: x[1])
    ans = 0
    current = 0
    for l, r in schedule:
        if l >= current:
            ans += 1

            current = r
    print(ans)


if __name__ == '__main__':
    main()
