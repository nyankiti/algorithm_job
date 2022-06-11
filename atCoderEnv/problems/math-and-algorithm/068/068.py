from sys import stdin
"""
集合の数 n の包除原理
"""


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def lcm(x, y):
    return x*y // gcd(x, y)


def main():
    N, K = map(int, stdin.readline().split())
    *V, = map(int, stdin.readline().split())

    yojishou = 0
    for i in range(2 ** K):
        temp_lcm = 1
        parity = 0
        for j in range(K):
            if ((i >> j) & 1):
                parity += 1
                temp_lcm = lcm(temp_lcm, V[j])
        if parity % 2 == 0:
            yojishou -= (N//temp_lcm)
        else:
            yojishou += (N//temp_lcm)

    yojishou += N

    print(yojishou)


if __name__ == '__main__':
    main()
