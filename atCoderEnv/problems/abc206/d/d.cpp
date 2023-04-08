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

class UnionFind {
public:
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

private:
    vector<int> parents;
};

int main() {
    int N;
    cin >> N;
    vi A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    UnionFind uf = UnionFind(200005);
    int ans = 0;
    for (int i = 0; i < N / 2; i++) {
        // cout << A[i] << " " << A[N - i - 1] << endl;
        if (!uf.is_same(A[i], A[N - i - 1])) {
            ans += 1;
            uf.unite(A[i], A[N - i - 1]);
        }
    }
    cout << ans << endl;
    return 0;
}