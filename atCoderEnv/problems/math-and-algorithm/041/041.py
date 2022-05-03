from sys import stdin


def main():
    T = int(stdin.readline())
    N = int(stdin.readline())
    shift = [0]*T
    for _ in range(N):
        L, R = map(int, stdin.readline().split())
        shift[L] += 1
        if R < T:
            shift[R] -= 1

    temp_shift_num = 0
    for shift_num in shift:
        temp_shift_num += shift_num
        print(temp_shift_num)


if __name__ == '__main__':
    main()
