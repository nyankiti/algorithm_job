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

int N, X, A[100009];

int bi_search(int x) {
  int L = 1, R = N;
  while (L <= R) {
    int M = (L + R) / 2;
    if (X == A[M]) return M;
    if (X < A[M]) {
      R = M - 1;
    } else {
      L = M + 1;
    }
  }
  return -1;
}
int main() {
  cin >> N >> X;
  rep(i, 1, N + 1) cin >> A[i];
  int ans = bi_search(X);
  cout << ans << endl;

  return 0;
}