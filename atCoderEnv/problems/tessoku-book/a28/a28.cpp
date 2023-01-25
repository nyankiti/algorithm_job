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

int N, A[100009];
char T[100009];
int main() {
  cin >> N;
  rep(i, 1, N + 1) cin >> T[i] >> A[i];
  int ans = 0;
  rep(i, 1, N + 1) {
    if (T[i] == '+') {
      ans += A[i];
    } else if (T[i] == '-') {
      ans -= A[i];
    } else {
      ans *= A[i];
    }
    if (ans < 0) {
      ans += 10000;
    }
    ans %= 10000;
    cout << ans << endl;
  }
  return 0;
}