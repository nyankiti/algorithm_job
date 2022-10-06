from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    D, N = map(int, stdin.readline().split())
    max_hours = [24]*(D)
    for _ in range(N):
        L, R, H = map(int, stdin.readline().split())
        for i in range(L, R+1):
            max_hours[i-1] = min(max_hours[i-1], H)
    max_hours.sort(reverse=True)
    print(sum(max_hours))


if __name__ == '__main__':
    main()
