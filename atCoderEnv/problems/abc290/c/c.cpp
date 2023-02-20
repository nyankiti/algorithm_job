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
  int N, K, A[300009];
  cin >> N >> K;
  rep(i, 1, N + 1) cin >> A[i];
  // 0 ~ K-1 が全て含まれている場合は K が答えとなる
  // => 0 から順にk-1まで含まれているものを数える
  map<int, bool> visited;
  rep(i, 1, N + 1) visited[A[i]] = true;

  rep(i, 0, K) {
    if (visited[i] == false) {
      cout << i << endl;
      return 0;
    }
  }
  cout << K << endl;
  return 0;
}