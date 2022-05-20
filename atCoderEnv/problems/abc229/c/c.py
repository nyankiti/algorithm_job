from sys import stdin


def main():
    N, W = map(int, stdin.readline().split())
    A = []
    # bはaを並び替えても参照しやすくするため、辞書型とする

    for _ in range(N):
        a, b = map(int, stdin.readline().split())
        A.append([a, b])

    # 貪欲法(最も美味しいチーズから順番にとっていく)
    A.sort(reverse=True, key=lambda x: x[0])

    ans = 0
    for i in range(len(A)):
        if A[i][1] <= W:
            ans += A[i][1] * A[i][0]
            W -= A[i][1]
        else:
            ans += A[i][0]*W
            W = 0

    print(ans)


if __name__ == '__main__':
    main()
