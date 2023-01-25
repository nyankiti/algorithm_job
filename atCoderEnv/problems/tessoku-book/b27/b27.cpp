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

ll gcd(ll a, ll b) {
  while (a % b != 0) {
    int temp = a % b;
    a = b;
    b = temp;
  }
  return b;
}

ll A, B;
int main() {
  cin >> A >> B;
  // cout << __gcd(A, B) << endl;
  cout << A * B / gcd(max(A, B), min(A, B)) << endl;
  return 0;
}