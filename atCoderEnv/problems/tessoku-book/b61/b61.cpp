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

int N, M, A[100009], B[100009];
vi G[100009];
int main() {
  cin >> N >> M;
  rep(i, 1, M + 1) cin >> A[i] >> B[i];
  rep(i, 1, M + 1) {
    G[A[i]].push_back(B[i]);
    G[B[i]].push_back(A[i]);
  }
  int ans = -1, max_num = 0;
  rep(i, 1, N + 1) {
    if (max_num < G[i].size()) {
      max_num = G[i].size();
      ans = i;
    }
  }
  cout << ans << endl;

  return 0;
}