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

int main() {
    int N, M, a, b;
    cin >> N >> M;
    vector<vector<int>> G(N);
    for (int i = 0; i < M; i++) {
        cin >> a >> b;
        a--;
        b--;
        G[a].push_back(b); // {b, c} として Edge Struct を省略して宣言している
        G[b].push_back(a);
    }
    vector<int> dist(N, INF);
    queue<int> q;
    q.push(0);
    dist[0] = 0;
    vector<int> q_order;
    while (q.size()) {
        int from = q.front();
        q.pop();
        q_order.push_back(from);
        for (int to : G[from]) {
            if (dist[to] != INF)
                continue;
            dist[to] = dist[from] + 1;
            q.push(to);
        }
    }

    // BFSした後のdist配列の性質を利用してDPする。
    vector<int> dp(N);
    dp[0] = 1;
    for (int from : q_order) {
        for (int to : G[from]) {
            if (dist[to] == dist[from] + 1) {
                dp[to] = (dp[to] + dp[from]) % MOD;
            }
        }
    }
    cout << dp[N - 1] << endl;

    return 0;
}