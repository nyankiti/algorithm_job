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
vector<ll> Dijkstra(const Graph& graph, int start, int goal) {
  int N = graph.size();
  vector<ll> dist(N + 1, 1LL << 60);
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
  int N, M, A, B, C, D;
  cin >> N >> M;
  Graph graph(N + 1);
  // int型で扱うため、コストを10000倍にする
  rep(i, 1, M + 1) {
    cin >> A >> B >> C >> D;
    graph[A].push_back({B, 10000 * C - (D == 1 ? 1 : 0)});
    graph[B].push_back({A, 10000 * C - (D == 1 ? 1 : 0)});
  }
  vector<ll> dist = Dijkstra(graph, 1, N);
  int ans_dist = (dist[N] + 9999) / 10000;
  int tree_num = ans_dist * 10000 - dist[N];
  cout << ans_dist << " " << tree_num << endl;
  return 0;
}