from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(input())
    K = int(input())
    LR = []
    for _ in range(N):
        l, r = list(map(int, input().split()))
        LR.append([l, r+K])

    # [ simulate ]
    # < find maxR >
    maxR = 0
    for _, r in LR:
        maxR = max(r, maxR)
    # < create schedule >
    scLR = []
    for l, r in LR:
        scLR.append([l, r])
    # < from left >
    scLR.sort(key=lambda x: (x[1], x[0]))
    # simulate
    preR = 0
    totC = 0
    totL = [0] * (maxR+1)
    for nowL, nowR in scLR:
        if preR <= nowL:
            totC += 1
            totL[nowR] = totC
            preR = nowR
    # update count
    for i in range(maxR):
        totL[i+1] = max(totL[i], totL[i+1])
    # < from right >
    scLR.sort(key=lambda x: (x[0], x[1]))
    scLR.reverse()
    # simulate
    preL = maxR
    totC = 0
    totR = [0] * (maxR+1)
    for nowL, nowR in scLR:
        if nowR <= preL:
            totC += 1
            totR[nowL] = totC
            preL = nowL
    # update count
    for i in range(maxR, 0, -1):
        totR[i-1] = max(totR[i], totR[i-1])

    # [ output ]
    for l, r in LR:
        cnt = totL[l] + 1 + totR[r]
        print(cnt)


if __name__ == '__main__':
    main()
