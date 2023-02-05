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

int N, M;
vi G[100009];
bool visited[100009];

void dfs(int v) {
  visited[v] = true;
  for (int adj : G[v]) {
    if (visited[adj] == false) {
      dfs(adj);
    }
  }
}

int main() {
  cin >> N >> M;
  rep(i, 1, N + 1) visited[i] = false;
  rep(i, 0, M) {
    int a, b;
    cin >> a >> b;
    G[a].push_back(b);
    G[b].push_back(a);
  }
  dfs(1);
  rep(i, 1, N + 1) {
    if (visited[i] == false) {
      cout << "The graph is not connected." << endl;
      return 0;
    }
  }
  cout << "The graph is connected." << endl;
  return 0;
}