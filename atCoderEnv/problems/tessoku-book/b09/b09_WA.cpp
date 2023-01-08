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
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

int A[100009], B[100009], C[100009], D[100009];
int grid[1509][1509], ruiseki[1509][1509];
int main() {
  int N, ans = 0;
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i] >> B[i] >> C[i] >> D[i];
  rep(i, 0, 1509) rep(j, 0, 1509) {
    ruiseki[i][j] = 0;
    grid[i][j] = 0;
  }
  rep(i, 1, N + 1) {
    ruiseki[A[i]][B[i]] += 1;
    ruiseki[A[i]][D[i] + 1] -= 1;
    ruiseki[C[i] + 1][B[i]] -= 1;
    ruiseki[C[i] + 1][D[i] + 1] += 1;
  }
  rep(i, 1, 1509) {
    rep(j, 1, 1509) { grid[i][j] = grid[i][j - 1] + ruiseki[i][j]; }
  }
  rep(j, 1, 1509) {
    rep(i, 1, 1509) { grid[i][j] = grid[i - 1][j] + grid[i][j]; }
  }
  rep(j, 1, 1505) {
    rep(i, 1, 1505) {
      if (grid[i][j] > 0 && grid[i + 1][j] > 0 && grid[i][j + 1] > 0 &&
          grid[i + 1][j + 1] > 0)
        ans++;
    }
  }
  cout << ans << endl;

  return 0;
}