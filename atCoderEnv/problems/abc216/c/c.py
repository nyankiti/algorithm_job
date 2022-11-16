from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    ans_rev = []
    while N != 1:
        if N % 2 == 0:
            N //= 2
            ans_rev.append("B")
        else:
            N -= 1
            ans_rev.append("A")
    N -= 1
    ans_rev.append("A")

    print("".join(list(reversed(ans_rev))))


if __name__ == '__main__':
    main()
