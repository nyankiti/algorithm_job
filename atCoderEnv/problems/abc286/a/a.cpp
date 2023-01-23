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

int N, P, Q, R, S, A[109];
int main() {
  cin >> N >> P >> Q >> R >> S;
  rep(i, 1, N + 1) cin >> A[i];
  int diff = R - P;
  rep(i, P, Q + 1) { swap(A[i], A[i + diff]); }
  rep(i, 1, N + 1) cout << A[i] << " ";
  cout << endl;

  return 0;
}