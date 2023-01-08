#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using pii = pair<int, int>;
/* macro */
#define rep(i, n) for (int i = 0; i < (n); ++i)

int main() {
  int A, B;
  cin >> A >> B;
  bool ans = false;
  for (int i = A; i <= B; i++) {
    if (100 % i == 0) {
      ans = true;
    }
  }
  cout << (ans ? "Yes" : "No") << endl;
  return 0;
}