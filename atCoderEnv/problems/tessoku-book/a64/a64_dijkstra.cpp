#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;  // 二次元vector
using vs = vector<string>;
using pii = pair<int, int>;
/* macro */
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

struct Edge {
  int to;    // 行き先
  int cost;  // コスト
};
using Graph = vector<vector<Edge>>;
vector<int> Dijkstra(const Graph& graph, int start, int goal) {
  int N = graph.size();
  vector<int> dist(N + 1, 2000000000);
  vector<bool> kakutei(N + 1, false);
  // (コスト、id)のペアを自動的に大きい順に取り出せる
  priority_queue<pii, vector<pii>, greater<pii>> Q;

  // ダイクストラ法
  dist[start] = 0;
  Q.push(make_pair(dist[start], 1));
  while (!Q.empty()) {
    int pos = Q.top().second;
    Q.pop();

    if (kakutei[pos]) continue;

    kakutei[pos] = true;
    for (Edge adj : graph[pos]) {
      int adj_id = adj.to;
      int cost = adj.cost;
      if (dist[adj_id] > dist[pos] + cost) {
        dist[adj_id] = dist[pos] + cost;
        Q.push(make_pair(dist[adj_id], adj_id));
      }
    }
  }
  return dist;
}
int main() {
  int N, M, a, b, c;
  cin >> N >> M;
  Graph G(N + 1);
  rep(i, 0, M) {
    cin >> a >> b >> c;
    G[a].push_back({b, c});  // {b, c} として Edge Struct を省略して宣言している
    G[b].push_back({a, c});
  }
  // 初期化
  vector<int> dist = Dijkstra(G, 1, N);
  rep(i, 1, N + 1) cout << (dist[i] == 2000000000 ? -1 : dist[i]) << endl;
  return 0;
}