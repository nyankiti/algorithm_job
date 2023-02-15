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
  int N, M, c, a;
  vi A[19];
  cin >> N >> M;
  rep(i, 0, M) {
    cin >> c;
    rep(j, 0, c) {
      cin >> a;
      A[i].push_back(a);
    }
  }

  int ans = 0;
  // bit 全探索
  for (int bit = 0; bit < (1 << M); ++bit) {
    bool ok = true;
    vector<bool> visited(N + 1, false);
    for (int i = 0; i < M; ++i) {
      if (bit & (1 << i)) {  // 列挙に i が含まれるか
        // 含まれる時、その集合に入っている数字をvisitedに記録する
        for (int val : A[i]) {
          visited[val] = true;
        }
      }
    }
    rep(i, 1, N + 1) {
      if (visited[i] == false) ok = false;
    }
    if (ok) ans += 1;
  }
  cout << ans << endl;
  return 0;
}