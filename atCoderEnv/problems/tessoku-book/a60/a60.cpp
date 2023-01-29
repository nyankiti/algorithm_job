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
  int N, A[200009];
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i];
  stack<pii> kessan;  // 常に降順に並んでいる
  // 初期値の設定
  kessan.push(make_pair(A[1], 1));
  cout << -1 << " ";

  rep(i, 2, N + 1) {
    while (!kessan.empty() && kessan.top().first <= A[i]) {
      kessan.pop();
    }
    if (kessan.empty()) {
      cout << -1 << " ";
    } else {
      cout << kessan.top().second << " ";
    }

    kessan.push(make_pair(A[i], i));
  }
  cout << endl;
  return 0;
}