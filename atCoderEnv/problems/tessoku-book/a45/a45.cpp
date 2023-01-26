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
  int N;
  char C;
  string A;
  cin >> N >> C >> A;
  int score = 0;
  for (char a : A) {
    if (a == 'B') score += 1;
    if (a == 'R') score += 2;
    // if (a == 'W') score += 0;
  }
  int target_score = 0;
  if (C == 'B') target_score = 1;
  if (C == 'R') target_score = 2;
  cout << (score % 3 == target_score ? "Yes" : "No") << endl;
  return 0;
}