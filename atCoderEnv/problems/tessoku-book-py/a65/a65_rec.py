from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    tree = [[] for _ in range(N)]
    for i, a in enumerate(A):
        # Aはa_2から始まるので、頂点番号を一つずらす必要がある
        v = i+1
        tree[a-1].append(v)
    # 頂点 v に何人の部下がいるかを記録する
    lookup = {}

    def rec(v):
        if v in lookup:
            return lookup[v]

        if len(tree[v]) == 0:
            # 部下がいない時
            return 0
        else:
            # 部下の人数
            sub_num = 0
            for sub_v in tree[v]:
                if (len(tree[sub_v]) == 0):
                    sub_num += 1
                else:
                    sub_num += rec(sub_v)+1
            lookup[v] = sub_num
            return lookup[v]

    for i in range(N):
        print(rec(i), end=" ")


if __name__ == '__main__':
    main()
