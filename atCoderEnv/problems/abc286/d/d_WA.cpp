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

int N, X, A[59], B[59];
int main() {
  cin >> N >> X;
  // keyを大きい順で並べる
  map<int, int, greater<int>> coins;
  rep(i, 1, N + 1) cin >> A[i] >> B[i];
  rep(i, 1, N + 1) coins[A[i]] = B[i];
  for (auto itr = coins.begin(); itr != coins.end(); itr++) {
    // cout << itr->first << endl;
    int rest_num = itr->second;
    while (rest_num > 0 && X >= itr->first) {
      X -= itr->first;
      rest_num -= 0;
    }
  }
  cout << (X == 0 ? "Yes" : "No") << endl;
  return 0;
}