#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using pii = pair<int, int>;
/* macro */
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

int main() {
  int N, K, ans = 0;
  cin >> N >> K;
  rep(i, 1, N + 1) rep(j, 1, N + 1) {
    if (K - (i + j) <= N && K - (i + j) > 0) {
      ans += 1;
    }
  }
  cout << ans << endl;
  return 0;
}