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
#define rep_a(i, a, n) for (int i = (a); i < (n); ++i)

int main() {
  int T, N, L, R, worker_num = 0, shift[500009];
  cin >> T >> N;
  rep(i, T + 1) { shift[i] = 0; }
  rep(i, N) {
    cin >> L >> R;
    shift[L] += 1;
    shift[R] -= 1;
  }
  rep(i, T) {
    worker_num += shift[i];
    cout << worker_num << endl;
  }
  return 0;
}