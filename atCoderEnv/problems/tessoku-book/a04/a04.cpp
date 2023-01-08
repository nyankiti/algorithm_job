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
  int N;
  cin >> N;
  string ans;
  for (int x = 9; x >= 0; x--) {
    int wari = (1 << x);
    ans += to_string((N / wari) % 2);
    // cout << (N / wari) % 2;
  }
  // cout << endl;
  cout << ans << endl;
  return 0;
}