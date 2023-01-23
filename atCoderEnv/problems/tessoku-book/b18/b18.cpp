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

int N, S, A[69];
bool dp[69][61000];
int main() {
  cin >> N >> S;
  rep(i, 1, N + 1) cin >> A[i];
  // dpテーブルの初期化
  rep(i, 0, N + 1) rep(j, 0, S + 1) dp[i][j] = false;
  rep(i, 0, N + 1) dp[i][0] = true;
  rep(i, 1, N + 1) {
    rep(j, 1, S + 1) {
      if (dp[i - 1][j]) dp[i][j] = true;
      if (j - A[i] >= 0 && dp[i - 1][j - A[i]]) {
        dp[i][j] = true;
      }
    }
  }

  if (!dp[N][S]) {
    cout << -1 << endl;
    return 0;
  }

  // 経路の復元
  int current_sum = S, current_pos = N;
  vi P;
  while (current_sum > 0) {
    if (dp[current_pos - 1][current_sum - A[current_pos]]) {
      P.push_back(current_pos);
      current_sum -= A[current_pos];
    }
    current_pos -= 1;
  }
  reverse(P.begin(), P.end());
  cout << P.size() << endl;
  rep(i, 0, P.size()) cout << P[i] << " ";
  return 0;
}