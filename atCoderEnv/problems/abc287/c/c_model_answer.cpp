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

// 一つでも条件を満たさない場合に Noを返すような問題では、
// mainで別にsolve関数を作って、条件を満たさなかったらすぐに
// false を返すよいう実装にすると書きやすい。
bool solve() {
  cin >> N >> M;
  vi deg(N);
  // 連結はunion findで管理
  dsu uf(N);
  rep(i, 0, M) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    deg[u] += 1;
    deg[v] += 1;
    uf.merge(u, v);
  }

  int one_deg_node_cnt = 0;
  rep(i, 0, N) {
    if (deg[i] == 0 || deg[i] > 2) return false;
    if (deg[i] == 1) one_deg_node_cnt += 1;
  }
  if (one_deg_node_cnt != 2) return false;

  if (uf.size(0) != N) return false;

  return true;
}

int main() {
  cout << (solve() ? "Yes" : "No") << endl;
  return 0;
}