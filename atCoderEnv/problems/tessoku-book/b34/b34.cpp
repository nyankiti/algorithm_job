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

ll N, X, Y, A[100009];
int main() {
  cin >> N >> X >> Y;
  rep(i, 1, N + 1) cin >> A[i];
  int XOR_sum = 0;
  rep(i, 1, N + 1) {
    if (A[i] % 5 == 0 || A[i] % 5 == 1) XOR_sum ^= 0;
    if (A[i] % 5 == 2 || A[i] % 5 == 3) XOR_sum ^= 1;
    if (A[i] % 5 == 4) XOR_sum ^= 2;
  }
  cout << (XOR_sum == 0 ? "Second" : "First") << endl;
  return 0;
}