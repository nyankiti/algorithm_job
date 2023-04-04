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

vector<int> Dijkstra(const vector<vector<int>> &graph, int start, int goal) {
    int N = graph.size();
    vector<int> dist(N, INF);
    vector<bool> kakutei(N, false);
    // (コスト、id)のペアを自動的に大きい順に取り出せる
    priority_queue<pii, vector<pii>, greater<pii>> Q;

    // ダイクストラ法
    dist[start] = 0;
    Q.push(make_pair(dist[start], start));
    while (!Q.empty()) {
        int pos = Q.top().second;
        Q.pop();

        if (kakutei[pos])
            continue;

        kakutei[pos] = true;
        for (int adj : graph[pos]) {
            if (dist[adj] > dist[pos] + 1) {
                dist[adj] = dist[pos] + 1;
                Q.push(make_pair(dist[adj], adj));
            }
        }
    }
    return dist;
}

int N, Q, a, b, c, d;
int main() {
    cin >> N >> Q;
    vector<vector<int>> G(N, vector<int>());
    for (int i = 0; i < N - 1; i++) {
        cin >> a >> b;
        a--;
        b--;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    vector<int> dist = Dijkstra(G, 0, N - 1);
    for (int i = 0; i < Q; i++) {
        cin >> c >> d;
        c--;
        d--;
        cout << (abs(dist[c] - dist[d]) % 2 != 0 ? "Road" : "Town") << endl;
    }
    return 0;
}