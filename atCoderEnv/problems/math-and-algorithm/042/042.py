from sys import stdin


def main():
    N = int(stdin.readline())

    divisors_lens = [0]*N
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            divisors_lens[j-1] += 1
    # print(divisors_lens)
    ans = 0
    for i, count in enumerate(divisors_lens):
        ans += (i+1)*count

    print(ans)


if __name__ == '__main__':
    main()
