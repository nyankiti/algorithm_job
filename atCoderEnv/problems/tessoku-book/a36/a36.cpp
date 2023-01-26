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

int N, K;
int main() {
  cin >> N >> K;
  cout << ((2 * (N - 1) <= K && K % 2 == 0) ? "Yes" : "No") << endl;
  return 0;
}