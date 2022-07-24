from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    *X, = map(int, stdin.readline().split())
    ruiseki_X = []
    x_sum = 0
    for x in X:
        x_sum += x
        ruiseki_X.append(x_sum)

    bonus = {}
    bonus_count_list = []
    for i in range(M):
        C, Y = map(int, stdin.readline().split())
        bonus[C] = Y
        bonus_count_list.append(C)

    # bonus_count_list.sort()

    # n 番目のコイントスで、得られる(最大値, カウンタの値)
    dp_front = []
    dp_back = []
    # 1回目の値を初期値として格納
    dp_front.append((X[0], 1))
    dp_back.append((0, 0))
    if 1 in bonus_count_list:
        dp_front[0] = (X[0]+bonus[1], 1)

    for i in range(1, N):
        next_val = max(dp_front[i-1], dp_back[i-1], key=lambda x: x[0])
        # 裏が出た場合は連続ボーナスをもらえる可能性がないので即決される
        dp_back.append((next_val[0], 0))

        # 表が出た場合の最大値を連続ボーナスも考慮して算出する
        candidate_1 = (next_val[0]+X[i], next_val[1]+1)
        candidate_2 = (0, 0)
        for c in bonus_count_list:

            if candidate_1[1] == c:
                candidate_1 = (candidate_1[0] + bonus[c], candidate_1[1])

            # c 回前で裏が出た場合をシュミレートし、値が高くなれば採用する
            if len(dp_front) >= c:
                temp_val = dp_back[i-c][0]

                temp_val += (ruiseki_X[i] - ruiseki_X[i-c])

                for sub_c in bonus_count_list:
                    if sub_c > c:
                        break
                    temp_val += bonus[sub_c]

                if candidate_2[0] < temp_val:
                    candidate_2 = (temp_val, c)

        if candidate_1[0] < candidate_2[0]:
            dp_front.append(candidate_2)
        else:
            dp_front.append(candidate_1)

    # print(dp_front)
    # print(dp_back)
    print(dp_front[-1][0])


if __name__ == '__main__':
    main()
