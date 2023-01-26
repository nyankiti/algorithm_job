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
  int N, height_from_L[3009], height_from_R[3009];
  string S;
  cin >> N >> S;
  rep(i, 0, N) {
    height_from_L[i] = 1;
    height_from_R[i] = 1;
  }
  rep(i, 0, N - 1) {
    if (S[i] == 'A') {
      height_from_L[i + 1] = height_from_L[i] + 1;
    }
  }
  for (int i = N - 1; i >= 0; i--) {
    if (S[i] == 'B') {
      height_from_R[i] = height_from_R[i + 1] + 1;
    }
  }
  int ans = 0;
  rep(i, 0, N) ans += max(height_from_L[i], height_from_R[i]);
  cout << ans << endl;
  return 0;
}