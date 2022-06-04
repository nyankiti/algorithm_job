from sys import stdin

N = 1048576


def main():
    A = [-1]*N
    Q = int(stdin.readline())
    # 自分に最も近い、書き換えられていない番号を見つけるための補助配列』 です。Pi=i は、その番号がまだ書き換えられていないことを示します。
    # うまく P を書き換えることで、P の要素をたどって書き換えられていない番号を見つけようというアイデアです。
    P = list(range(N))

    for _ in range(Q):
        t, x = map(int, stdin.readline().split())

        if t == 1:
            h = x % N
            pos = h
            visited = [pos]
            while A[pos] != -1:
                pos = P[pos]
                visited.append(pos)

            # 数列Aの書き換え
            A[pos] = x

            # まだ書き換えられていない、最も近いpositionで、visitedしたPを書き換え
            new_p = P[(pos + 1) % N]
            for u in visited:
                P[u] = new_p

        elif t == 2:
            print(A[x % N])


if __name__ == '__main__':
    main()
