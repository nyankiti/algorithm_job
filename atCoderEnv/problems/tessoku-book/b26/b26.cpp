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

int N;
bool prime_table[1000009];
int main() {
  cin >> N;
  rep(i, 0, 1000009) prime_table[i] = true;
  rep(i, 2, sqrt(1000009) + 1) {
    if (prime_table[i]) {
      for (int j = i * 2; j < 1000009; j += i) {
        prime_table[j] = false;
      }
    }
  }
  rep(i, 2, N + 1) {
    if (prime_table[i]) cout << i << endl;
  }
  return 0;
}