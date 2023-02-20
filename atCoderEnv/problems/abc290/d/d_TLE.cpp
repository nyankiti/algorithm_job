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

void solve(int N, int D, int K) {
  vector<bool> mass(N, false);
  mass[0] = true;
  int A = 0, x, label_cnt = 1;

  rep(i, 0, N) {
    if (label_cnt == K) {
      cout << A << endl;
      return;
    }
    x = (A + D) % N;

    while (mass[x] == true) {
      x = (x + 1) % N;
    }
    mass[x] = true;
    label_cnt += 1;
    A = x;
  }
}

int main() {
  int T;
  cin >> T;
  rep(i, 0, T) {
    int n, d, k;
    cin >> n >> d >> k;
    solve(n, d, k);
  }
  return 0;
}