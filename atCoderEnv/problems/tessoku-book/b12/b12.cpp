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

double f(double x) { return (x * x * x) + x; }

int main() {
  int N;
  cin >> N;
  double left = 0, right = 100, middle, temp;
  rep(i, 0, 20) {
    // C++ の割り算は切り捨てて整数となる
    middle = (left + right) / 2.0;
    temp = f(middle);
    if (temp <= 1.0 * N) {
      left = middle;
    } else {
      right = middle;
    }
  }
  printf("%.12f", middle);
  return 0;
}