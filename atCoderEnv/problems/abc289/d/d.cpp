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

int main() {
  int static N, M, X, A[19], B[100009];
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i];
  cin >> M;
  rep(i, 1, M + 1) cin >> B[i];
  cin >> X;
  // dp -1 の時、そこに餅がある。1の時、到達可能。 0 の時、未探索
  vector<int> static dp(X + 1, 0);

  rep(i, 1, M + 1) dp[B[i]] = -1;
  dp[0] = 1;
  // 探索
  rep(i, 0, X + 1) {
    if (dp[i] == 1) {
      rep(j, 1, N + 1) {
        if (i + A[j] <= X && dp[i + A[j]] != -1) {
          dp[i + A[j]] = 1;
        }
      }
    }
  }
  cout << (dp[X] == 1 ? "Yes" : "No") << endl;

  return 0;
}