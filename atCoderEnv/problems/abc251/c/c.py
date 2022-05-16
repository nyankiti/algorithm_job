from sys import stdin


def main():
    N = int(stdin.readline())

    poems = {}

    for i in range(N):
        S, T = stdin.readline().split()
        T = int(T)

        # di.get(S, T)
        if S in poems:
            # poems[S] = False
            pass
        else:
            # (点数, index) という形式で記録する
            poems[S] = (T, i+1)

    scores = []
    for S, value in poems.items():
        if value:
            scores.append([S, value])

    scores.sort(key=lambda x: x[1][0], reverse=True)
    # print(scores)
    print(scores[0][1][1])


if __name__ == '__main__':
    main()
