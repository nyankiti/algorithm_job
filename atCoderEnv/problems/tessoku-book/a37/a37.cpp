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

ll N, M, B, A[200009], C[200009];
int main() {
  cin >> N >> M >> B;
  rep(i, 1, N + 1) cin >> A[i];
  rep(i, 1, M + 1) cin >> C[i];
  ll ans = 0, A_sum = 0, C_sum = 0;
  rep(i, 1, N + 1) A_sum += A[i];
  rep(i, 1, M + 1) C_sum += C[i];
  ans = (A_sum * M) + (C_sum * N) + B * M * N;
  cout << ans << endl;

  return 0;
}