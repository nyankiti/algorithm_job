#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>; // 二次元vector
using vs = vector<string>;
using pii = pair<int, int>;
/* macro */
#define MOD 1000000007
#define MOD2 998244353
#define INF ((1 << 30) - 1)
#define LINF (1LL << 60)
// 非常に小さい値を表す epsilon。浮動小数展比較において、誤差の範囲を表すために使用する。10^(-10)を表している。
#define EPS (1e-10)

/*
UnionFindとDFSで解けそう
*/
class UnionFind {
public:
    vector<int> parents;
    explicit UnionFind(size_t n) : parents(n, -1) {}

    // 頂点 i のrootのインデックスを返す
    int find(int i) {
        if (parents[i] < 0) {
            return i;
        }
        parents[i] = find(parents[i]);
        return parents[i];
    }

    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) {
            // union by size(小さい方を子にしてメモリを削減)
            if (parents[a] < parents[b])
                swap(a, b);
            parents[a] += parents[b];
            parents[b] = a;
        }
    }

    bool is_same(int a, int b) { return (find(a) == find(b)); }

    int size(int i) { return -parents[find(i)]; }
};

int N, M, A, C;
char B, D;

int main() {
    cin >> N >> M;
    UnionFind uf = UnionFind(N);
    int cc_cnt = 0, cycle_cnt = 0;
    for (int i = 0; i < M; i++) {
        cin >> A >> B >> C >> D;
        A--;
        C--;
        if (uf.is_same(A, C)) {
            cycle_cnt += 1;
        }
        uf.unite(A, C);
    }
    for (auto p : uf.parents) {
        if (p < 0)
            cc_cnt += 1;
    }
    cout << cycle_cnt << " " << cc_cnt - cycle_cnt << endl;
    return 0;
}