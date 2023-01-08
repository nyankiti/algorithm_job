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
#define rep(i, n) for (int i = 0; i < (n); ++i)

int main() {
  string N;  // for文を回すためにiterativeなstring型で受けとる
  cin >> N;
  int ans = 0;

  reverse(N.begin(), N.end());

  for (int i = N.size() - 1; i >= 0; i--) {
    if (N[i] == '1') {
      ans += (1 << i);
    }
  }
  cout << ans << endl;

  return 0;
}