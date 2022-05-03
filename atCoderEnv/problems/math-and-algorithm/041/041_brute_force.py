from sys import stdin


def main():
    T = int(stdin.readline())
    N = int(stdin.readline())
    shift = [0]*T
    for _ in range(N):
        L, R = map(int, stdin.readline().split())
        for i in range(L, R):
            shift[i] += 1

    # print(shift)

    for shift_num in shift:
        print(shift_num)


if __name__ == '__main__':
    main()
