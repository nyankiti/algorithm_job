def f(b):
    return a ** 3 + b * a ** 2 + a * b ** 2 + b ** 3


N = int(input())
ans = float("INF")
for a in range(10 ** 6 + 5):
    ng = -1
    ok = 10 ** 6 + 5
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid) >= N:
            ok = mid
        else:
            ng = mid
    ans = min(ans, f(ok))
print(ans)
