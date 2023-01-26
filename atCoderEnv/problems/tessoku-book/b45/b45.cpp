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
  ll a, b, c;
  cin >> a >> b >> c;
  ll pos_sum = 0, neg_sum = 0;
  if (a > 0)
    pos_sum += a;
  else
    neg_sum += a;
  if (b > 0)
    pos_sum += b;
  else
    neg_sum += b;
  if (c > 0)
    pos_sum += c;
  else
    neg_sum += c;
  cout << (pos_sum + neg_sum == 0 ? "Yes" : "No") << endl;
  return 0;
}