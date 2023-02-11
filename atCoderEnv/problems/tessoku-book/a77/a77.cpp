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

int N, L, K, A[100009];

bool check(int x) {
  int cnt = 0, last_kireme = 0;
  rep(i, 1, N + 1) {
    if (A[i] - last_kireme >= x && L - A[i] >= x) {
      cnt += 1;
      last_kireme = A[i];
    }
  }
  return cnt >= K;
}

int main() {
  cin >> N >> L >> K;
  rep(i, 1, N + 1) cin >> A[i];
  int left = 1, right = 1000000000;
  while (left < right) {
    int mid = (left + right + 1) / 2;
    bool ans = check(mid);
    if (ans) {
      left = mid;
    } else {
      right = mid - 1;
    }
  }
  cout << left << endl;
  return 0;
}