from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *P, = map(int, stdin.readline().split())

    '''
    全ての回転パターンを計算しないといけない。その計算方法を速くする工夫を考える。

    全ての回転パターンの中で、 i 番目の人が得点に影響するのは、料理が i-1,i,i+1の位置にある3回だけである
    => 影響する範囲が少ない！

    各料理に注目した時、どの回し方にした時に得点が増えるか、という逆の見方をすると計算量が削減できる!
    (ヒストグラムを作るイメージ)
    '''
    counter = [0]*N
    for i in range(N):
        counter[(P[i] - i) % N] += 1
        counter[(P[(i+1) % N] - i) % N] += 1
        counter[(P[(i-1) % N] - i) % N] += 1
    print(max(counter))


if __name__ == '__main__':
    main()
