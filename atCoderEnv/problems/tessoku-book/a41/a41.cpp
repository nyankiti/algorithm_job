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
  bool ans = false;
  char prev;
  int cnt = 0;
  rep(i, 0, N) {
    if (S[i] == prev) {
      cnt += 1;
    } else {
      prev = S[i];
      cnt = 1;
    }
    if (cnt == 3) ans = true;
  }
  cout << (ans ? "Yes" : "No") << endl;
  return 0;
}