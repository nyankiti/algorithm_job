from sys import stdin


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        return 2**(x-1) % x == 1
        # return pow(2, x - 1, x) == 1


def judge(n, thirds):
    for third in thirds:
        q, mod = divmod(n, third)
        if int(mod) == 0:
            if q < third ** (1/3):
                if is_prime(q):
                    # print(n)
                    return True


def main():
    N = int(stdin.readline())
    thirds = []
    for i in range(2, int(N**(1/3))):
        if is_prime(i):
            thirds.append(i**3)

    # print(thirds)

    ans = 0
    for i in range(N+1):
        if judge(i, thirds):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
