from sys import stdin


def main():
    h1, h2, h3, w1, w2, w3 = map(int, stdin.readline().split())

    w1_candidates = []
    w2_candidates = []
    w3_candidates = []
    h1_candidates = []
    h2_candidates = []
    h3_candidates = []

    for i in range(1, 29):
        for j in range(1, 29):
            for k in range(1, 29):
                if i+j+k == w1:
                    w1_candidates.append([i, j, k])
                if i+j+k == w2:
                    w2_candidates.append([i, j, k])
                if i+j+k == w3:
                    w3_candidates.append([i, j, k])
                if i+j+k == h1:
                    h1_candidates.append([i, j, k])
                if i+j+k == h2:
                    h2_candidates.append([i, j, k])
                if i+j+k == h3:
                    h3_candidates.append([i, j, k])

    ans = 0

    for w1_torio in w1_candidates:
        w1_h1_candidates = []
        w1_h2_candidates = []
        w1_h3_candidates = []
        for h1_torio in h1_candidates:
            if w1_torio[0] == h1_torio[0]:
                w1_h1_candidates.append(h1_torio)

        for h2_torio in h2_candidates:
            if w1_torio[1] == h2_torio[0]:
                w1_h2_candidates.append(h2_torio)

        for h3_torio in h3_candidates:
            if w1_torio[2] == h3_torio[0]:
                w1_h3_candidates.append(h3_torio)

        # この縦のトリオで他のw2, w3の条件を満たすかをチェック
        for h1_ in w1_h1_candidates:
            for h2_ in w1_h2_candidates:
                if w2-h1_[1]-h2_[1] > 30 or w3-h1_[2]-h2_[2] > 30:
                    continue

                for h3_ in w1_h3_candidates:
                    # if [h1_[1], h2_[1], h3_[1]] in w2_candidates:
                    #     ans += 1
                    for w2_ in w2_candidates:
                        if w2_[0] != h1_[1]:
                            continue
                        if w2_[1] != h2_[1]:
                            continue
                        if w2_[2] != h3_[1]:
                            continue
                        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
