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

int N, A[100009], B[100009];
int main() {
  cin >> N;
  vi T;
  rep(i, 1, N + 1) cin >> A[i];
  rep(i, 1, N + 1) T.push_back(A[i]);
  sort(T.begin(), T.end());

  T.erase(unique(T.begin(), T.end()), T.end());

  rep(i, 1, N + 1) {
    auto it = lower_bound(T.begin(), T.end(), A[i]);
    int num_size_index = it - T.begin();
    B[i] = num_size_index + 1;
  }
  rep(i, 1, N + 1) {
    if (i >= 2) cout << " ";
    cout << B[i];
  }
  cout << endl;
  return 0;
}