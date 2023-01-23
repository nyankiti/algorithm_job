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

void dfs(int pos, vi li) {
  rep(i, pos, N) {
    if (li.back() < A[pos]) {
      li.push_back(A[pos]);
      dfs(pos + 1, li);
      li.pop_back();
    }
  }
}

int main() {
  cin >> N;
  vi L;
  rep(i, 1, N + 1) {
    cin >> A[i];
    dp[i] = 1;
  }
  return 0;
}