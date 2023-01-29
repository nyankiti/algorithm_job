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

int ketawa(int num) {
  string str = to_string(num);
  int ans = 0;
  // (int)char は 対応する char型の ascii値
  // を返すので、数字が欲しい場合は、'0'との差を取る必要がある
  rep(i, 0, str.size()) { ans += ((int)str[i] - (int)'0'); }
  return ans;
}

int main() {
  int N, K;
  cin >> N >> K;

  static int dp[30][300009];
  rep(i, 1, N + 1) { dp[0][i] = i - ketawa(i); }
  rep(d, 1, 30) {
    rep(i, 1, N + 1) { dp[d][i] = dp[d - 1][dp[d - 1][i]]; }
  }

  rep(i, 1, N + 1) {
    int current_num = i;
    for (int d = 29; d >= 0; d--) {
      if ((K / (1 << d)) % 2 == 1) current_num = dp[d][current_num];
    }
    cout << current_num << endl;
  }

  return 0;
}