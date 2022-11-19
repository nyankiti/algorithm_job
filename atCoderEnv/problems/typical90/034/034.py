from collections import defaultdict, deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    ans = 0
    # しゃくとり法で計算量を削減する
    dq = deque()
    # 現在選択中の数の種類
    selected = []
    # しゃくとり法で探索中の範囲にそれぞれの数字がいくつ含まれているかをカウントする
    counter = defaultdict(int)
    for i in range(N):
        dq.append(A[i])
        counter[A[i]] += 1
        if counter[A[i]] == 1:
            selected.append(A[i])

        while len(selected) > K:
            popped = dq.popleft()
            counter[popped] -= 1
            if counter[popped] == 0:
                selected.remove(popped)

        ans = max(ans, len(dq))

    print(ans)


if __name__ == '__main__':
    main()
