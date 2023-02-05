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

int N, A[100009], ans[100009];
vi tree[100009];

int dfs(int v) {
  if (tree[v].size() == 0) {
    ans[v] = 0;
    return 1;
  }

  int child_sum = 0;
  for (int child : tree[v]) {
    child_sum += dfs(child);
  }
  ans[v] = child_sum;
  return child_sum + 1;
}

int main() {
  cin >> N;
  rep(i, 2, N + 1) cin >> A[i];
  // 上司 => 部下 の方向にのみ edge を追加
  rep(i, 2, N + 1) { tree[A[i]].push_back(i); }
  rep(i, 1, N + 1) ans[i] = 0;
  dfs(1);
  rep(i, 1, N + 1) cout << ans[i] << " ";
  cout << endl;
  return 0;
}