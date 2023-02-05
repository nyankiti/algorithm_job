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

int N, M, a, b;
vi G[100009];
int dist[100009];
deque<int> deq;
int main() {
  cin >> N >> M;
  rep(i, 0, M) {
    cin >> a >> b;
    G[a].push_back(b);
    G[b].push_back(a);
  }
  rep(i, 1, N + 1) dist[i] = -1;

  deq.push_back(1);
  dist[1] = 0;
  while (!deq.empty()) {
    int popped = deq.front();
    deq.pop_front();
    for (int adj : G[popped]) {
      if (dist[adj] == -1) {
        dist[adj] = dist[popped] + 1;
        deq.push_back(adj);
      }
    }
  }
  rep(i, 1, N + 1) cout << dist[i] << endl;
  return 0;
}