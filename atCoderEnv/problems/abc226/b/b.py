from sys import stdin


def main():
    N = int(stdin.readline())

    counter = {}

    for _ in range(N):
        L, *a, = map(int, stdin.readline().split())
        t = tuple([L, *a])
        counter[t] = counter.get(t, 0) + 1

    print(len(counter.keys()))


if __name__ == '__main__':
    main()
