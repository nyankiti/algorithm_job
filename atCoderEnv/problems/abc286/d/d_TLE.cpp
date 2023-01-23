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

int N, X, A[59], B[59];

bool dfs(int pos, int temp_sum) {
  if (pos == N) {
    rep(i, 0, B[pos] + 1) {
      if (temp_sum + (A[pos] * i) == X) {
        return true;
      }
    }
    return false;
  }
  bool is_fit_X = false;
  rep(i, 0, B[pos] + 1) {
    // A[pos] を i個選んだ場合
    is_fit_X = is_fit_X || dfs(pos + 1, temp_sum + A[pos] * i);
  }
  return is_fit_X;
}

int main() {
  cin >> N >> X;
  rep(i, 1, N + 1) cin >> A[i] >> B[i];
  cout << (dfs(1, 0) ? "Yes" : "No") << endl;
  return 0;
}