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

int N, A, B;
bool state[100009];
int main() {
  cin >> N >> A >> B;

  rep(i, 0, A) state[i] = false;
  rep(i, A, N + 1) {
    if (i - B >= 0) {
      if (state[i - A] == false || state[i - B] == false) {
        state[i] = true;
      } else {
        state[i] = false;
      }
    } else {
      if (state[i - A] == false) {
        state[i] = true;
      } else {
        state[i] = false;
      }
    }
  }
  cout << (state[N] ? "First" : "Second") << endl;
  return 0;
}