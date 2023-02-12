#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vvl = vector<vi>;  // 二次元vector
using vs = vector<string>;
using pii = pair<int, int>;
/* macro */
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

int N, A, B;
vi G[200009];
bool visited[200009];
vi ans;

void dfs(int v, int parent = -1) {
  ans.push_back(v);
  for (int adj : G[v]) {
    if (adj == parent) continue;
    dfs(adj, v);
    ans.push_back(v);
  }
}

int main() {
  cin >> N;
  rep(i, 1, N) {
    cin >> A >> B;
    G[A].push_back(B);
    G[B].push_back(A);
  }
  rep(i, 1, N + 1) {
    sort(G[i].begin(), G[i].end());
    visited[i] = false;
  }

  dfs(1);

  for (int val : ans) cout << val << endl;
  return 0;
}