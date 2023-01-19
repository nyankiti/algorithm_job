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
  string S, alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  cin >> S;
  map<char, int> alphabet_mapping;
  rep(i, 0, alphabet.size()) { alphabet_mapping[alphabet[i]] = i + 1; }
  // 26進数を考える
  reverse(S.begin(), S.end());
  ll ans = 0;
  rep(i, 0, S.size()) { ans += (powl(26, i)) * alphabet_mapping[S[i]]; }
  cout << ans << endl;
  return 0;
}