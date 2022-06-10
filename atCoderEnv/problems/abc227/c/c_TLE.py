from sys import stdin

"""
探索範囲の絞り込みが浅い！
"""


def main():
    N = int(stdin.readline())

    ans = 0

    for i in range(1, N+1):
        for j in range(i, N+1):
            if i*j > N:
                break
            for k in range(j, N+1):
                if i*j*k > N:
                    break
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
