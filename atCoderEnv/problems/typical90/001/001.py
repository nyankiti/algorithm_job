from sys import stdin


def canDivideScoreM(pieces, m, K):
    temp_sum = 0
    count = 0

    for piece in pieces:
        temp_sum += piece
        if temp_sum >= m:
            temp_sum = 0
            count += 1

    if count >= K+1:
        return True
    else:
        return False


def main():
    N, L = map(int, stdin.readline().split())
    K = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    pieces = []
    pieces.append(A[0])
    for i in range(len(A)-1):
        pieces.append(A[i+1]-A[i])
    pieces.append(L-A[-1])
    # print(pieces)
    # print(sum(pieces))

    ng = 0
    ok = L
    while ng <= ok:
        mid = (ok + ng)//2
        if canDivideScoreM(pieces, mid, K):
            ng = mid + 1
        else:
            ok = mid - 1
    print(ok)


if __name__ == '__main__':
    main()
