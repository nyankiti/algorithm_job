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

int N, M, A[100009], B[100009];
vi G[100009];
int main() {
  cin >> N >> M;
  rep(i, 1, M + 1) cin >> A[i] >> B[i];
  rep(i, 1, M + 1) {
    G[A[i] - 1].push_back(B[i] - 1);
    G[B[i] - 1].push_back(A[i] - 1);
  }
  rep(i, 0, N) {
    cout << i + 1 << ": {";
    rep(j, 0, G[i].size()) {
      if (j == G[i].size() - 1) {
        cout << G[i][j] + 1;
      } else {
        cout << G[i][j] + 1 << ", ";
      }
    }
    cout << "}" << endl;
  }
  return 0;
}