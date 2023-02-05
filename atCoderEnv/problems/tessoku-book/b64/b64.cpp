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
bool kakutei[100009];
int dist[100009];
// (距離、node id) を優先度付きキューで管理
priority_queue<pii, vector<pii>, greater<pii>> Q;
int main() {
  cin >> N >> M;
  rep(i, 0, M) {
    cin >> a >> b >> c;
    G[a].push_back(make_pair(b, c));
    G[b].push_back(make_pair(a, c));
  }

  rep(i, 1, N + 1) {
    kakutei[i] = false;
    dist[i] = 2000000000;
  }
  dist[1] = 0;
  Q.push(make_pair(dist[1], 1));
  while (!Q.empty()) {
    int curr = Q.top().second;
    Q.pop();

    if (kakutei[curr] == true) continue;
    kakutei[curr] = true;

    for (auto val : G[curr]) {
      int adj = val.first;
      int cost = val.second;
      if (dist[adj] >= dist[curr] + cost) {
        dist[adj] = dist[curr] + cost;
        Q.push(make_pair(dist[adj], adj));
      }
    }
  }
  // 経路復元
  int curr = N;
  deque<int> ans;
  ans.push_front(N);

  while (curr != 1) {
    for (auto val : G[curr]) {
      int adj = val.first;
      int cost = val.second;
      if (dist[adj] == dist[curr] - cost) {
        ans.push_front(adj);
        curr = adj;
        break;
      }
    }
  }
  for (auto itr = ans.begin(); itr != ans.end(); itr++) {
    cout << *itr << " ";
  }
  cout << endl;
  return 0;
}