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
  int N, K;
  string S;
  cin >> N >> K >> S;
  int on_count = 0;
  for (auto val : S)
    if (val == '1') on_count += 1;
  cout << (on_count % 2 == K % 2 ? "Yes" : "No") << endl;
  return 0;
}