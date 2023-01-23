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

int N, A[100009], dp[100009];
int main() {
  cin >> N;
  vi L;
  rep(i, 1, N + 1) {
    cin >> A[i];
    dp[i] = 1;
  }
  rep(i, 1, N + 1) {
    auto itr = lower_bound(L.begin(), L.end(), A[i]);
    int pos = itr - L.begin();
    if (itr == L.end()) {
      // 最も高い場合、Lが増える
      dp[i] = pos;
      L.push_back(A[i]);
    } else {
      L[pos] = min(L[pos], A[i]);
    }
  }
  cout << L.size() << endl;
  return 0;
}