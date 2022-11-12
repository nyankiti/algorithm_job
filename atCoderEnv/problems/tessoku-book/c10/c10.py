from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

MOD = 1000000007


def main():
    W = int(stdin.readline())
    if W == 1:
        print(12)
        return
    if W == 2:
        print(84)
        return

    if W % 2 == 0:
        # print(49**(W//2-1)*84)
        ans = pow(49, W//2-1, mod=MOD)*84
        print(ans % MOD)
    else:
        # 49**(W//2)*12
        ans = pow(49, W//2, mod=MOD)*12
        print(ans % MOD)


if __name__ == '__main__':
    main()
