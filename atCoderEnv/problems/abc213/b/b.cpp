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
int main() {
  cin >> N;
  vector<pii> A;
  rep(i, 0, N) {
    int a;
    cin >> a;
    A.push_back(make_pair(a, i + 1));
  }
  sort(A.begin(), A.end(), greater<pii>());
  // rep(i, 0, N) cout << A[i].first << " " << A[i].second << endl;

  cout << A[1].second << endl;
  return 0;
}