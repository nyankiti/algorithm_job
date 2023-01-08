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
#define rep_a(i, a, n) for (int i = (a); i < (n); ++i)

int main() {
  int D, N, L, R, count = 0, diff[100009];
  cin >> D >> N;
  rep(i, N) {
    cin >> L >> R;
    diff[L]++;
    diff[R + 1]--;
  }
  rep_a(i, 1, D + 1) {
    count += diff[i];
    cout << count << endl;
  }
  return 0;
}