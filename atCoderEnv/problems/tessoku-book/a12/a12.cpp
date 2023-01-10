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

int A[100009];

int main() {
  int N, K, ans = -1;
  cin >> N >> K;
  rep(i, 1, N + 1) cin >> A[i];
  ll left = 0, right = 1000000000, middle, count;

  while (left < right) {
    // C++ の割り算は切り捨てて整数となる
    middle = (left + right) / 2;
    count = 0;
    rep(i, 1, N + 1) count += middle / A[i];
    if (count < K) {
      left = middle + 1;
    } else {
      right = middle;
    }
  }
  cout << left << endl;
  return 0;
}