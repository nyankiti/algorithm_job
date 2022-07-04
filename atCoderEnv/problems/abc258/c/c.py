from sys import stdin


def main():
    N, Q = map(int, stdin.readline().split())
    S = input()
    start_pos = 0

    for _ in range(Q):
        *query, = map(int, stdin.readline().split())

        if query[0] == 1:
            start_pos += query[1]
        elif query[0] == 2:
            print(S[(query[1] - start_pos - 1) % N])


if __name__ == '__main__':
    main()
