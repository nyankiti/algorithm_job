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

int N, M, A[19], X[109], Y[109], Z[109];
vi G[1039];
int dist[1039];

void dfs(int v, int goal) {
  if (v == goal) return;

  for (int adj : G[v]) {
    if (dist[adj] == -1) {
      dist[adj] = dist[v] + 1;
      dfs(adj, goal);
    }
  }

  return;
}

int main() {
  cin >> N >> M;
  rep(i, 1, N + 1) cin >> A[i];
  rep(i, 1, M + 1) cin >> X[i] >> Y[i] >> Z[i];

  // 2進数を利用してグラフで表現し,dfsする

  rep(bit, 0, 1 << N) {
    rep(i, 1, M + 1) {
      // 状態 bit から X[i], Y[i], Z[i]を反転させた後の遷移先
      int next_bit = bit;
      if ((bit / (1 << (X[i] - 1))) % 2 == 1) {
        next_bit -= 1 << (X[i] - 1);
      } else {
        next_bit += 1 << (X[i] - 1);
      }
      if ((bit / (1 << (Y[i] - 1))) % 2 == 1) {
        next_bit -= 1 << (Y[i] - 1);
      } else {
        next_bit += 1 << (Y[i] - 1);
      }
      if ((bit / (1 << (Z[i] - 1))) % 2 == 1) {
        next_bit -= 1 << (Z[i] - 1);
      } else {
        next_bit += 1 << (Z[i] - 1);
      }
      G[bit].push_back(next_bit);
    }
  }
  int initial_state = 0;
  rep(i, 1, N + 1) if (A[i] == 1) initial_state += (1 << (i - 1));
  rep(i, 0, 1 << N) dist[i] = -1;

  dist[initial_state] = 0;
  // dfs
  // dfs(initial_state, ((1 << N) - 1));

  // bfs
  deque<int> deq;
  deq.push_back(initial_state);
  while (!deq.empty()) {
    int pos = deq.front();
    deq.pop_front();
    for (int adj : G[pos]) {
      if (dist[adj] == -1) {
        dist[adj] = dist[pos] + 1;
        deq.push_back(adj);
      }
    }
  }

  // rep(i, 0, 1 << N) { cout << dist[i] << " "; }
  // cout << endl;

  cout << dist[(1 << N) - 1] << endl;
  return 0;
}