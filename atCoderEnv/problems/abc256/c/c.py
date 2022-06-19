from sys import stdin


def main():
    h1, h2, h3, w1, w2, w3 = map(int, stdin.readline().split())

    w1_candidates = []
    w2_candidates = []
    w3_candidates = []

    for i in range(1, 29):
        for j in range(1, 29):
            for k in range(1, 29):
                if i+j+k == w1:
                    w1_candidates.append([i, j, k])
                if i+j+k == w2:
                    w2_candidates.append([i, j, k])
                if i+j+k == w3:
                    w3_candidates.append([i, j, k])

    ans = 0

    for w1_torio in w1_candidates:
        for w2_torio in w2_candidates:
            for w3_torio in w3_candidates:
                if w1_torio[0] + w2_torio[0] + w3_torio[0] == h1:
                    if w1_torio[1] + w2_torio[1] + w3_torio[1] == h2:
                        if w1_torio[2] + w2_torio[2] + w3_torio[2] == h3:
                            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
