from sys import stdin
import bisect


def main():
    N = int(stdin.readline())
    schedules = []

    for _ in range(N):
        L, R = map(int, stdin.readline().split())
        schedules.append([L, R])

    schedules.sort(key=lambda x: x[1])

    current_time = 0
    ans = 0
    for r in schedules:
        if current_time <= r[0]:
            ans += 1
            current_time = r[1]

    print(ans)


if __name__ == '__main__':
    main()
