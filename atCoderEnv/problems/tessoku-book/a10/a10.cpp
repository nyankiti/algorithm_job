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

int A[100009];
int ruiseki_max[100009], ruiseki_max_rev[100009];

int main() {
  int N, D, L, R;
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i];
  rep(i, 0, N + 2) {
    ruiseki_max[i] = 0;
    ruiseki_max_rev[i] = 0;
  }
  rep(i, 1, N + 1) { ruiseki_max[i] = max(ruiseki_max[i - 1], A[i]); }
  for (int i = N; i > 0; i--) {
    ruiseki_max_rev[i] = max(ruiseki_max_rev[i + 1], A[i]);
  }
  // デバッグ
  // rep(i, 1, N + 1) { cout << ruiseki_max[i] << endl; }
  cin >> D;
  rep(i, 1, D + 1) {
    cin >> L >> R;
    cout << max(ruiseki_max[L - 1], ruiseki_max_rev[R + 1]) << endl;
  }
  return 0;
}