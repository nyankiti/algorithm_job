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
  string S;
  cin >> S;
  // 26進数を考える
  reverse(S.begin(), S.end());
  ll ans = 0, digit = 1;
  rep(i, 0, S.size()) {
    ans += digit * ((S[i] - 'A') + 1);
    digit *= 26;
  }
  cout << ans << endl;
  return 0;
}