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
  static int N, X[100009], Y[100009], dp[100009];
  cin >> N;
  rep(i, 1, N + 1) cin >> X[i] >> Y[i];

  // pairの一つ目を昇順、二つ目を降順にしたい場合は、二つ目をマイナスにしておく
  vector<pii> temp;
  rep(i, 1, N + 1) temp.push_back(make_pair(X[i], -Y[i]));
  sort(temp.begin(), temp.end());

  vi A;
  for (auto val : temp) A.push_back(-val.second);

  // AについてLISを求める
  rep(i, 0, N + 1) dp[i] = 0;
  vi L;
  rep(i, 0, A.size()) {
    auto itr = lower_bound(L.begin(), L.end(), A[i]);
    int pos = itr - L.begin();
    if (itr == L.end()) {
      dp[i + 1] = pos;
      L.push_back(A[i]);
    } else {
      L[pos] = min(L[pos], A[i]);
    }
  }
  cout << L.size() << endl;
  return 0;
}