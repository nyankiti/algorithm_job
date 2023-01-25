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

int Q, X[10009];
bool prime_table[300009];
int main() {
  cin >> Q;
  rep(i, 1, Q + 1) cin >> X[i];
  rep(i, 0, 300009) prime_table[i] = true;
  rep(i, 2, sqrt(300009) + 1) {
    if (prime_table[i]) {
      for (int j = i * 2; j < 300009; j += i) {
        prime_table[j] = false;
      }
    }
  }
  rep(i, 1, Q + 1) cout << (prime_table[X[i]] ? "Yes" : "No") << endl;
  return 0;
}