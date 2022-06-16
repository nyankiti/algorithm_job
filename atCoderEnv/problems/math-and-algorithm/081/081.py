from sys import stdin


def main():
    N = int(stdin.readline())
    ans = 0
    coins = [10000, 5000, 1000]
    for coin in coins:
        while N >= coin:
            ans += 1
            N -= coin
    print(ans)


if __name__ == '__main__':
    main()
