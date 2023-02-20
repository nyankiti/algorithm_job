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

int N, K;
string S;
int main() {
  cin >> N >> K >> S;
  string ans = "";
  int ans_count = 0;
  for (char val : S) {
    if (val == 'o') {
      if (ans_count < K) {
        ans += 'o';
        ans_count += 1;
      } else {
        ans += 'x';
      }
    } else {
      ans += 'x';
    }
  }
  cout << ans << endl;
  return 0;
}