from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())

    result = []

    for _ in range(2*N):
        *A, = list(stdin.readline())
        result.append(A)

    order = [[i+1, 0] for i in range(2*N)]

    def janken(player_1, player_2, i):
        p_1_hand = result[player_1[0]-1][i]
        p_2_hand = result[player_2[0]-1][i]

        # あいこの場合
        if p_1_hand == p_2_hand:
            return
        if (p_1_hand == "G" and p_2_hand == "C") or (p_1_hand == "C" and p_2_hand == "P") or (p_1_hand == "P" and p_2_hand == "G"):
            player_1[1] += 1
        else:
            player_2[1] += 1

    for i in range(M):
        for j in range(0, 2*N, 2):
            player_1 = order[j]
            player_2 = order[j+1]
            janken(player_1, player_2, i)
        # sortは安定なので、まずplayer idで並び替えを先に行い、その後に順位で並び替えると希望通りにsortされる
        order.sort(key=lambda x: x[0])
        order.sort(key=lambda x: x[1], reverse=True)

    print(order)
    for val in order:
        print(val[0])


if __name__ == '__main__':
    main()
