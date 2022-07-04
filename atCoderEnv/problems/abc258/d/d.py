import math
from sys import stdin


def main():
    N, X = map(int, stdin.readline().split())

    games = []
    for _ in range(N):
        A, B = map(int, stdin.readline().split())
        games.append([A, B])

    # i番目のゲームまで行くためにかかるコスト、その時点での最小のB
    kaisa = []
    temp_sum = 0
    temp_min_B = math.inf
    for A, B in games:
        temp_sum += A+B
        temp_min_B = min(temp_min_B, B)
        kaisa.append([temp_sum, temp_min_B])

    ans = math.inf
    for index, val in enumerate(kaisa):
        temp_X = X
        cost, min_B = val
        temp_X -= index+1
        temp_ans = cost
        temp_ans += min_B*temp_X
        ans = min(ans, temp_ans)

    print(ans)


if __name__ == '__main__':
    main()
