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

int N, M, a, b, c;
vector<pii> G[100009];
// ダイクストラ法
int dist[100009];
bool kakutei[100009];
// (コスト、id)のペアを自動的に大きい順に取り出せる
priority_queue<pii, vector<pii>, greater<pii>> Q;
int main() {
  cin >> N >> M;
  rep(i, 0, M) {
    cin >> a >> b >> c;
    G[a].push_back(make_pair(b, c));
    G[b].push_back(make_pair(a, c));
  }
  // 初期化
  rep(i, 1, N + 1) {
    dist[i] = 2000000000;
    kakutei[i] = false;
  }
  // ダイクストラ法
  dist[1] = 0;
  Q.push(make_pair(dist[1], 1));
  while (!Q.empty()) {
    int pos = Q.top().second;
    Q.pop();

    if (kakutei[pos]) continue;

    kakutei[pos] = true;
    for (pii adj : G[pos]) {
      int adj_id = adj.first;
      int cost = adj.second;
      if (dist[adj_id] > dist[pos] + cost) {
        dist[adj_id] = dist[pos] + cost;
        Q.push(make_pair(dist[adj_id], adj_id));
      }
    }
  }

  rep(i, 1, N + 1) cout << (dist[i] == 2000000000 ? -1 : dist[i]) << endl;
  return 0;
}