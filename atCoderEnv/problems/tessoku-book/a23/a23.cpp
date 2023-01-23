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

int main() {
  int N, M, A[109][109];
  cin >> N >> M;
  rep(i, 1, M + 1) rep(j, 1, N + 1) cin >> A[i][j];
  /*
   bitDP
   dp[i][S] => i枚のクーポン券の中から何枚か選び、無料で買える品物の集合が S
   となる際の、選んだクーポン券の最小値
  */
  int dp[109][1030];
  rep(i, 0, M + 1) rep(j, 0, (1 << N)) dp[i][j] = 1000000000;
  dp[0][0] = 0;
  rep(i, 1, M + 1) {
    rep(j, 0, (1 << N)) {
      // 集合 j の際に既に買える商品を管理する
      int already[19];
      rep(k, 1, N + 1) {
        if ((j / (1 << (k - 1))) % 2 == 0)
          already[k] = 0;
        else
          already[k] = 1;
      }

      // 既に無料 or i番目のクーポンによって無料化できる集合を v で表す。
      int v = 0;
      rep(k, 1, N + 1) {
        if (already[k] == 1 || A[i][k] == 1) v += (1 << (k - 1));
      }

      dp[i][j] = min(dp[i][j], dp[i - 1][j]);
      // i番目のクーポンを使うことで、集合 v が無料になるので、集合 v へ遷移
      dp[i][v] = min(dp[i][v], dp[i - 1][j] + 1);
    }
  }
  cout << (dp[M][(1 << N) - 1] == 1000000000 ? -1 : dp[M][(1 << N) - 1])
       << endl;

  return 0;
}