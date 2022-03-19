from sys import stdin

N, X = map(int, stdin.readline().split())


balls = []
ans = 0


for _ in range(N):
    L, *A, = map(int, stdin.readline().split())
    balls.append(A)


def dfs(position, product):
    global ans

    if position == N:
        # positionがNの場合は探索終了する
        if product == X:
            ans += 1
        return

    for a in balls[position]:
        if X < product * a:
            # 次に進んでも答えが見つからないことが確定する
            continue
        dfs(position+1, product*a)


dfs(0, 1)


print(ans)
