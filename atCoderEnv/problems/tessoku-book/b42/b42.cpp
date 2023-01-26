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

ll N, A[100009], B[100009];
int main() {
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i] >> B[i];
  // 正と負が混じる場合は最大値にならない気がする
  ll ans = 0, temp = 0;
  rep(i, 1, N + 1) {
    if (A[i] + B[i] > 0) {
      temp += (A[i] + B[i]);
    }
  }
  ans = max(ans, temp);
  temp = 0;

  rep(i, 1, N + 1) {
    if (A[i] - B[i] > 0) {
      temp += (A[i] - B[i]);
    }
  }
  ans = max(ans, temp);
  temp = 0;

  rep(i, 1, N + 1) {
    if (-A[i] + B[i] > 0) {
      temp += (-A[i] + B[i]);
    }
  }
  ans = max(ans, temp);
  temp = 0;
  rep(i, 1, N + 1) {
    if (-A[i] - B[i] > 0) {
      temp += (-A[i] - B[i]);
    }
  }
  ans = max(ans, temp);
  temp = 0;
  cout << ans << endl;
  return 0;
}