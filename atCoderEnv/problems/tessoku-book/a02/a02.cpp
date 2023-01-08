#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using pii = pair<int, int>;
/* macro */
#define rep(i, n) for (int i = 0; i < (n); ++i)

int main() {
  int N, X, A[109];
  bool ans = false;
  cin >> N >> X;
  rep(i, N) { cin >> A[i]; }
  rep(i, N) {
    if (A[i] == X) {
      ans = true;
    }
  }
  if (ans) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  return 0;
}