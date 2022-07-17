from sys import stdin


def main():
    N, X, Y, Z = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    *B, = map(int, stdin.readline().split())

    # [番号、数学の点数、英語の点数, 合計点] として管理する
    scores = []
    for i in range(N):
        scores.append([i, A[i], B[i], A[i]+B[i]])

    # i番目の人が受かったかどうか
    gouhi = [False]*N

    # 数学が高いX人
    scores.sort(key=lambda x: x[1], reverse=True)
    for i in range(X):
        gouhi[scores[i][0]] = True

    # print(gouhi)

    # 英語が高い人
    scores.sort(key=lambda x: x[0])
    scores.sort(key=lambda x: x[2], reverse=True)

    i = 0
    eigo_count = 0
    while eigo_count < Y:
        if gouhi[scores[i][0]] == False:
            gouhi[scores[i][0]] = True
            eigo_count += 1
        i += 1
    # print(gouhi)

    # 合計点が高い人 Z 人
    scores.sort(key=lambda x: x[0])
    scores.sort(key=lambda x: x[3], reverse=True)

    i = 0
    all_count = 0
    while all_count < Z:
        if gouhi[scores[i][0]] == False:
            gouhi[scores[i][0]] = True
            all_count += 1
        i += 1
    # print(gouhi)

    # 答えの出力
    scores.sort(key=lambda x: x[0])
    for val in scores:
        if gouhi[val[0]]:
            print(val[0]+1)


if __name__ == '__main__':
    main()
