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

int main() {
  int N;
  string S;
  cin >> N >> S;
  rep(i, 1, N) {
    int l = 0;
    rep(k, 0, N - i) {
      if (S[k] != S[k + i])
        l += 1;
      else
        break;
    }
    cout << l << endl;
  }
  return 0;
}