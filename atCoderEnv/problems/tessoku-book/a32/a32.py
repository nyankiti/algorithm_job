from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, A, B = map(int, stdin.readline().split())
    # B+1 の倍数で相手に渡すようにする

    # 先手が勝つ場合をTrueとする
    state = [False]*(N+1)
    state[A] = True
    state[B] = True

    for i in range(N+1):
        if i < A:
            state[i] = False
        elif A < i and i < B:
            # 相手に負け状態で渡せる場合、勝つことができる
            if state[i-A] == False:
                state[i] = True
        else:
            if state[i-A] == False:
                state[i] = True
            if state[i-B] == False:
                state[i] = True

    print("First" if state[-1] else "Second")


if __name__ == '__main__':
    main()
