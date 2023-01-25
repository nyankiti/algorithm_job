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

int N, A[100009];
int main() {
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i];
  int XOR_sum = A[1];
  rep(i, 2, N + 1) XOR_sum = (XOR_sum ^ A[i]);
  cout << (XOR_sum == 0 ? "Second" : "First") << endl;
  return 0;
}