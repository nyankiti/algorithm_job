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

struct Edge {
    int to;   // 行き先
    int cost; // コスト
};
using Graph = vector<vector<Edge>>;
vector<int> Dijkstra(const Graph &graph, int start, int goal) {
    int N = graph.size();
    vector<int> dist(N + 1, INF);
    vector<int> num(N + 1, 0);
    vector<bool> kakutei(N + 1, false);
    // (コスト、id)のペアを自動的に大きい順に取り出せる
    priority_queue<pii, vector<pii>, greater<pii>> Q;

    // ダイクストラ法
    dist[start] = 0;
    num[start] = 1;
    Q.push(make_pair(dist[start], 1));
    while (!Q.empty()) {
        int pos = Q.top().second;
        Q.pop();

        if (kakutei[pos])
            continue;

        kakutei[pos] = true;
        for (Edge adj : graph[pos]) {
            int adj_id = adj.to;
            int cost = adj.cost;
            if (dist[adj_id] > dist[pos] + cost) {
                dist[adj_id] = dist[pos] + cost;
                num[adj_id] = num[pos];
                Q.push(make_pair(dist[adj_id], adj_id));
            } else if (dist[adj_id] == dist[pos] + cost) {
                num[adj_id] = (num[adj_id] + num[pos]) % MOD;
            }
        }
    }
    return num;
}

int main() {
    int N, M, a, b;
    cin >> N >> M;
    Graph G(N + 1);
    for (int i = 0; i < M; i++) {
        cin >> a >> b;
        G[a].push_back({b, 1}); // {b, c} として Edge Struct を省略して宣言している
        G[b].push_back({a, 1});
    }
    // 初期化
    vector<int> num = Dijkstra(G, 1, N);
    cout << num[N] << endl;

    // min_costで行けるパスを復元する過程で数える？？
    return 0;
}