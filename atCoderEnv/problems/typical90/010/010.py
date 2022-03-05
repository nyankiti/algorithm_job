from sys import stdin

N = int(stdin.readline())

data = {
    "first_cumulative_sum": [0]*(N+1),
    "second_cumulative_sum": [0]*(N+1),
    "others": [0]*(N+1),
}

for i in range(1, N+1):
    # i-1番目までの学績番号のi番目の累積和を反映
    for key in data:
        data[key][i] = data[key][i-1]

    # i番目の生徒のデータを反映
    C, P = map(int, stdin.readline().split())
    if C == 1:
        key = "first_cumulative_sum"
    elif C == 2:
        key = "second_cumulative_sum"
    else:
        key = "others"

    data[key][i] = data[key][i] + P


Q = int(stdin.readline())

for _ in range(Q):
    L, R = map(int, stdin.readline().split())

    # L-1番目より前の累積和を引く(L番目の生徒のデータは含む)
    print(data["first_cumulative_sum"][R] -
          data["first_cumulative_sum"][L-1], "", end="")
    print(data["second_cumulative_sum"][R] -
          data["second_cumulative_sum"][L-1])
