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

int N, M, A[200009];
int main() {
  cin >> N >> M;
  rep(i, 1, M + 1) cin >> A[i];
  map<int, int> minus_cnt;
  rep(i, 1, M + 1) minus_cnt[A[i]] += 1;
  rep(i, 1, N + 1) cout << M - minus_cnt[i] << endl;
  return 0;
}