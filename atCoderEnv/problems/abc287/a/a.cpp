#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;  // 二次元vector
using vs = vector<string>;
using pii = pair<int, int>;
/* macro */
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

int main() {
  int N;
  string S[109];
  cin >> N;
  rep(i, 1, N + 1) cin >> S[i];
  int for_sum = 0;
  rep(i, 1, N + 1) {
    if (S[i] == "For") {
      for_sum += 1;
    }
  }
  if (for_sum > N / 2) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}