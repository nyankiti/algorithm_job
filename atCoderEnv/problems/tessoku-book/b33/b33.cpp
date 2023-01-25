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

int N, H, W, A[100009], B[100009];
int main() {
  cin >> N >> H >> W;
  rep(i, 1, N + 1) cin >> A[i] >> B[i];

  int XOR_sum = 0;
  rep(i, 1, N + 1) XOR_sum = (XOR_sum ^ (A[i] - 1));
  rep(i, 1, N + 1) XOR_sum = (XOR_sum ^ (B[i] - 1));
  cout << (XOR_sum == 0 ? "Second" : "First") << endl;
  return 0;
}