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

int N, T, A[100009], B[100009];
vi G[100009];
bool visited[100009];
int depth[100009];
void dfs(int v) {
  visited[v] = true;
  // 部下がいない社員の階級は0
  if (G[v].size() == 0) {
    depth[v] = 0;
    return;
  }
  int max_sub_depth = 0;
  for (int adj : G[v]) {
    if (visited[adj] == false) {
      dfs(adj);
    }
    max_sub_depth = max(max_sub_depth, depth[adj]);
  }
  depth[v] = max_sub_depth + 1;
}
int main() {
  cin >> N >> T;
  rep(i, 1, N) cin >> A[i] >> B[i];
  rep(i, 1, N) {
    G[A[i]].push_back(B[i]);
    G[B[i]].push_back(A[i]);
  }
  rep(i, 1, N + 1) {
    depth[i] = 0;
    visited[i] = false;
  }
  dfs(T);
  rep(i, 1, N + 1) { cout << depth[i] - 1 << " "; }
  cout << endl;
  return 0;
}