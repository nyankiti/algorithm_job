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

int N, X, Y, A[100009], grundy[100009];
int main() {
  cin >> N >> X >> Y;
  rep(i, 1, N + 1) cin >> A[i];

  // Grundy数を求める
  rep(i, 0, 100009) {
    bool Transit[3] = {false, false, false};
    if (i >= X) Transit[grundy[i - X]] = true;
    if (i >= Y) Transit[grundy[i - Y]] = true;
    if (Transit[0] == false)
      grundy[i] = 0;
    else if (Transit[1] == false)
      grundy[i] = 1;
    else
      grundy[i] = 2;
  }
  int XOR_sum = 0;
  rep(i, 1, N + 1) XOR_sum = (XOR_sum ^ grundy[A[i]]);
  cout << (XOR_sum == 0 ? "Second" : "First") << endl;

  return 0;
}