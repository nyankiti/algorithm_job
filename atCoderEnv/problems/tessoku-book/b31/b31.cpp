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

ll N;
int main() {
  cin >> N;
  cout << (N / 3 + N / 5 + N / 7 + N / (3 * 5 * 7) - N / (3 * 5) - N / (5 * 7) -
           N / (7 * 3))
       << endl;
  return 0;
}