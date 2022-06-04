from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())

    current_scores = []

    for i in range(N):
        P1, P2, P3 = map(int, stdin.readline().split())
        current_scores.append([i,  P1 + P2 + P3])

    # 暫定の得点が大きい順に並べる
    current_scores.sort(key=lambda x: x[1], reverse=True)
    # print(current_scores)

    # 暫定でK番目の得点を記録
    k_point = current_scores[K-1][1]
    # print(k_point)

    result = []
    for data in current_scores:
        if data[1] >= k_point - 300:
            result.append([data[0], "Yes"])
        else:
            result.append([data[0], "No"])

    result.sort(key=lambda x: x[0])

    for data in result:
        print(data[1])


if __name__ == '__main__':
    main()
