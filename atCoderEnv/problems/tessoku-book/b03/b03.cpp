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
  int N, A[109];
  bool ans = false;
  cin >> N;
  rep(i, N) { cin >> A[i]; }
  for (int i = 0; i < N; ++i) {
    for (int j = i + 1; j < N; ++j) {
      for (int k = j + 1; k < N; ++k) {
        if (A[i] + A[j] + A[k] == 1000) {
          ans = true;
        }
      }
    }
  }
  cout << (ans ? "Yes" : "No") << endl;
  return 0;
}