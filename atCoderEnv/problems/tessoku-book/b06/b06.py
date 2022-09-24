from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    Q = int(stdin.readline())
    atari_count = 0
    atari_ruiseki = [atari_count]
    hazure_count = 0
    hazure_ruiseki = [hazure_count]

    for a in A:
        if a == 1:
            atari_count += 1
        else:
            hazure_count += 1
        atari_ruiseki.append(atari_count)
        hazure_ruiseki.append(hazure_count)

    for _ in range(Q):
        L, R = map(int, stdin.readline().split())
        a_count = atari_ruiseki[R] - atari_ruiseki[L-1]
        h_count = hazure_ruiseki[R] - hazure_ruiseki[L-1]

        if a_count == h_count:
            print("draw")
        elif a_count > h_count:
            print("win")
        else:
            print("lose")


if __name__ == '__main__':
    main()
