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

int N, K, a[100009];
bool state[100009];
int main() {
  cin >> N >> K;
  rep(i, 1, K + 1) cin >> a[i];
  rep(i, 0, N + 1) state[i] = false;

  rep(i, 1, N + 1) {
    rep(k, 1, K + 1) {
      if (i - a[k] >= 0 && state[i - a[k]] == false) {
        state[i] = true;
      }
    }
  }
  cout << (state[N] ? "First" : "Second") << endl;
  return 0;
}