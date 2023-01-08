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
  int N, Q, A[100009], ruiseki[100009], L[100009], R[100009];
  cin >> N >> Q;
  rep_a(i, 1, N + 1) { cin >> A[i]; }
  rep_a(i, 1, Q + 1) { cin >> L[i] >> R[i]; }

  ruiseki[0] = 0;
  rep_a(i, 1, N + 1) { ruiseki[i] = ruiseki[i - 1] + A[i]; }

  rep_a(i, 1, Q + 1) { cout << ruiseki[R[i]] - ruiseki[L[i] - 1] << endl; }

  return 0;
}