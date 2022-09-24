from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    # 右側からと左側からで、その時点での最大何人部屋からを記録する配列を作る
    max_capa_from_left = [0]
    max_capa_from_right = [0]
    temp_max = 0
    for i in range(N):
        temp_max = max(temp_max, A[i])
        max_capa_from_left.append(temp_max)
    temp_max = 0
    for i in range(N-1, -1, -1):
        temp_max = max(temp_max, A[i])
        max_capa_from_right.append(temp_max)

    D = int(stdin.readline())
    for _ in range(D):
        L, R = map(int, stdin.readline().split())
        # print(max_capa_from_left[:L], max_capa_from_left[L-1])
        # print(max_capa_from_right[:-(R)], max_capa_from_right[-(R+1)])

        print(max(max_capa_from_left[L-1], max_capa_from_right[-(R+1)]))


if __name__ == '__main__':
    main()
