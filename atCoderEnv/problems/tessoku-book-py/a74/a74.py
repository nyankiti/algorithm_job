from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def bubble_sort(data):
    tentou = 0
    for i in range(0, len(data)-1):
        for j in range(1, len(data)-i):
            if data[j-1] > data[j]:
                tentou += 1
                data[j], data[j-1] = data[j-1], data[j]  # インデックスj-1とjを入れ替える処理
    return tentou


def main():
    N = int(stdin.readline())
    P = [list(map(int, stdin.readline().split())) for _ in range(N)]
    w_li = []
    h_li = []
    for p in P:
        for val in p:
            if val != 0:
                h_li.append(val)
    for p in list(zip(*P)):
        for val in p:
            if val != 0:
                w_li.append(val)

    ans = 0
    ans += bubble_sort(h_li)
    ans += bubble_sort(w_li)
    print(ans)


if __name__ == '__main__':
    main()
