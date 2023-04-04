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

int N, Q, a, b, c, d;
vector<vector<int>> G;
vector<int> dep;
void dfs(int v, int _dep = 0, int p = -1) {
    dep[v] = _dep;
    for (int u : G[v]) {
        if (u == p)
            continue;
        dfs(u, _dep + 1, v);
    }
}
int main() {
    cin >> N >> Q;
    G.resize(N);
    dep.resize(N);
    for (int i = 0; i < N - 1; i++) {
        cin >> a >> b;
        a--;
        b--;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    dfs(0);
    for (int i = 0; i < Q; i++) {
        cin >> c >> d;
        c--;
        d--;
        int ans = (dep[c] + dep[d]) % 2;
        cout << (ans ? "Road" : "Town") << endl;
    }
    return 0;
}