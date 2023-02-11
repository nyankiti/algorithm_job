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

int N, A[69], B[69];
int main() {
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i];
  rep(i, 1, N + 1) cin >> B[i];
  sort(begin(A) + 1, begin(A) + N + 1);
  sort(begin(B) + 1, begin(B) + N + 1);
  reverse(begin(B) + 1, begin(B) + N + 1);

  int ans = 0;
  rep(i, 1, N + 1) ans += A[i] * B[i];
  cout << ans << endl;
  return 0;
}