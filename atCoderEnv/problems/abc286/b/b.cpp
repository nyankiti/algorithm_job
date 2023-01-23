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

int N;
string S, ans;
int main() {
  cin >> N >> S;
  rep(i, 0, N) {
    ans.push_back(S[i]);
    if (S[i] == 'n' && S[i + 1] == 'a') {
      ans.push_back('y');
    }
  }
  cout << ans << endl;
  return 0;
}