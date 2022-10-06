from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    N_digit = len(str(N))

    ans = 0
    for i in range(1, N_digit):
        count = int(str(9*(i-1)) + "0"*(i-2)) + int("1" + "0"*(i-1))
        # print(count)
        for i in range(1, 10):
            ans += i*count

    # ここのループを間に合わすことができない
    for i in range(10**(N_digit-1), N+1):
        # print(i, sum([int(num) for num in str(i)]))
        ans += sum([int(num) for num in str(i)])
    print(ans)


if __name__ == '__main__':
    main()
