from sys import stdin

N, Q = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())

shift_count = 0

for _ in range(Q):
    T, x, y = map(int, stdin.readline().split())

    if T == 1:
        A[(x-1-shift_count) % N], A[(y-1-shift_count) %
                                    N] = A[(y-1-shift_count) % N], A[(x-1-shift_count) % N]
        # print("xとyを入れ替え", A)
    elif T == 2:
        shift_count += 1
    elif T == 3:
        print(A[(x-1-shift_count) % N])
