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

int N, K;
string S[109];
int main() {
  cin >> N >> K;
  vector<string> vec_S;
  rep(i, 1, N + 1) {
    cin >> S[i];
    vec_S.push_back(S[i]);
  }
  sort(vec_S.begin(), vec_S.begin() + K);
  rep(i, 0, K) { cout << vec_S[i] << endl; }
  return 0;
}