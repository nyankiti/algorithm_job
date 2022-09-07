from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    min_A = A[0]
    max_A = A[-1]

    # 山に i 個石が残っている状態で先手が勝てるかどうか
    state = [False]*(K+1)

    for i in range(1, K+1):
        temp = False
        for a in A:
            if i == a:
                temp = True
            elif i - a > 0:
                # 相手に負け状態を渡せる場合、勝てる。
                if state[i-a] == False:
                    temp = True
            else:
                continue
        state[i] = temp

    # print(state[:21])
    print("First" if state[-1] else "Second")


if __name__ == '__main__':
    main()
